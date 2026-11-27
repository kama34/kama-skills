#!/usr/bin/env python3
"""Local, bounded, read-only Telegram history via the official TDLib JSON API."""

import argparse
import codecs
import ctypes
import ctypes.util
import fcntl
import getpass
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import warnings
import zipfile
from contextlib import contextmanager, nullcontext
from datetime import datetime, timezone
from xml.etree import ElementTree


STATE_DIR = Path.home() / "Library/Application Support/2030ai/telegram-chat-reader"
AUTH_READY = "authorizationStateReady"
CONNECTED = "connectionStateReady"
DEFAULT_LIMIT = 50
MAX_LIMIT = 200
MAX_PAGES = 40
WEEK = 7 * 86400
MAX_MEDIA_BYTES = 100 * 1024 * 1024
MAX_EXTRACTED_CHARS = 50_000
DEFAULT_MODEL = STATE_DIR / "models/ggml-small-q5_1.bin"
MEDIA_DEMUXERS = ("aac,ac3,aiff,amr,asf,avi,flac,flv,gif,matroska,mov,mp3,mpeg,mpegts,"
                  "ogg,rm,swf,tta,wav,webm,wv")
MEDIA_FIELDS = {
    "messageAnimation": ("animation", "animation", ".mp4"),
    "messageAudio": ("audio", "audio", ".mp3"),
    "messageDocument": ("document", "document", ".bin"),
    "messageSticker": ("sticker", "sticker", ".webp"),
    "messageVideo": ("video", "video", ".mp4"),
    "messageVideoNote": ("video_note", "video", ".mp4"),
    "messageVoiceNote": ("voice_note", "voice", ".ogg"),
}


class ReaderError(Exception):
    pass


class TDError(ReaderError):
    def __init__(self, method, code):
        self.code = code
        # TDLib diagnostics can contain private input or output.
        super().__init__(f"TDLib {method} failed (code {code}).")


def require_type(value, expected):
    if not isinstance(value, dict) or value.get("@type") != expected:
        raise ReaderError(f"TDLib returned an unexpected response for {expected}.")
    return value


def folder_title(folder):
    try:
        return folder["name"]["text"]["text"]
    except (KeyError, TypeError) as error:
        raise ReaderError("TDLib does not expose the current chat folder name schema.") from error


def list_key(chat_list):
    kind = chat_list["@type"]
    return kind, chat_list["chat_folder_id"] if kind == "chatListFolder" else None


def chat_metadata(chat):
    if not isinstance(chat.get("chat_lists"), list):
        raise ReaderError("TDLib does not expose evaluated chat membership. A current build is required.")
    return {
        "id": chat["id"],
        "title": chat["title"],
        "type": chat["type"],
        "lists": {list_key(item) for item in chat["chat_lists"]},
        "protected": chat["has_protected_content"],
    }


def active_usernames(obj):
    return tuple(name.lower() for name in (obj.get("usernames") or {}).get("active_usernames", ()))


class State:
    def __init__(self):
        self.auth = None
        self.connection = None
        self.connection_revision = 0
        self.folders = None
        self.chats = {}
        self.users = {}
        self.supergroups = {}

    def apply(self, update):
        kind = update["@type"]
        if kind == "updateAuthorizationState":
            self.auth = update["authorization_state"]["@type"]
        elif kind == "updateConnectionState":
            value = update["state"]["@type"]
            if self.connection != value:
                self.connection_revision += 1
                self.connection = value
        elif kind == "updateChatFolders":
            self.folders = [(item["id"], folder_title(item)) for item in update["chat_folders"]]
        elif kind == "updateNewChat":
            chat = chat_metadata(update["chat"])
            self.chats[chat["id"]] = chat
        elif kind == "updateUser":
            user = update["user"]
            name = " ".join(part for part in (user.get("first_name"), user.get("last_name")) if part)
            self.users[user["id"]] = (name or None, active_usernames(user))
        elif kind == "updateSupergroup":
            group = update["supergroup"]
            self.supergroups[group["id"]] = active_usernames(group)
        elif kind in (
            "updateChatTitle", "updateChatHasProtectedContent",
            "updateChatAddedToList", "updateChatRemovedFromList",
        ):
            chat = self.chats.get(update["chat_id"])
            if chat is None:
                return
            if kind == "updateChatTitle":
                chat["title"] = update["title"]
            elif kind == "updateChatHasProtectedContent":
                chat["protected"] = update["has_protected_content"]
            elif kind == "updateChatAddedToList":
                chat["lists"].add(list_key(update["chat_list"]))
            else:
                chat["lists"].discard(list_key(update["chat_list"]))


def json_bytes(value):
    return json.dumps(value, ensure_ascii=False).encode("utf-8")


class TDLib:
    def __init__(self):
        override = os.environ.get("TDJSON_LIBRARY")
        paths = (override,) if override else (
            "/opt/homebrew/opt/tdlib/lib/libtdjson.dylib",
            "/usr/local/opt/tdlib/lib/libtdjson.dylib",
            ctypes.util.find_library("tdjson"),
        )
        for path in paths:
            if not path:
                continue
            try:
                lib = ctypes.CDLL(path)
                lib.td_execute.argtypes = [ctypes.c_char_p]
                lib.td_execute.restype = ctypes.c_char_p
                lib.td_create_client_id.argtypes = []
                lib.td_create_client_id.restype = ctypes.c_int
                lib.td_send.argtypes = [ctypes.c_int, ctypes.c_char_p]
                lib.td_send.restype = None
                lib.td_receive.argtypes = [ctypes.c_double]
                lib.td_receive.restype = ctypes.c_char_p
                break
            except (OSError, AttributeError):
                continue
        else:
            raise ReaderError("Current TDLib JSON library was not found. See the skill setup.")
        self.lib = lib
        self.state = State()
        self.client_id = None
        self.serial = 0
        require_type(self.execute("setLogStream", log_stream={"@type": "logStreamEmpty"}), "ok")
        self.version = require_type(self.execute("getOption", name="version"), "optionValueString")["value"]
        if self.version == "1.8.0":
            raise ReaderError("TDLib 1.8.0 has an older schema. Install a current build.")

    def execute(self, method, **fields):
        reply = self.lib.td_execute(json_bytes({"@type": method, **fields}))
        if not reply:
            raise ReaderError(f"No synchronous TDLib response for {method}.")
        return json.loads(reply)

    def send(self, method, **fields):
        self.lib.td_send(self.client_id, json_bytes({"@type": method, **fields}))

    def receive(self, timeout):
        reply = self.lib.td_receive(timeout)
        if reply is None:
            return None
        result = json.loads(reply)
        if result.get("@client_id") == self.client_id and "@extra" not in result:
            self.state.apply(result)
        return result

    def drain(self):
        for _ in range(4096):
            if self.receive(0) is None:
                return
        raise ReaderError("TDLib updates are still arriving. Retry after synchronization.")

    def wait(self, predicate, *, seconds=30, failure="TDLib state did not become ready."):
        deadline = time.monotonic() + seconds
        while not predicate():
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise ReaderError(failure)
            self.receive(min(1, remaining))

    def request(self, method, *, timeout=30, **fields):
        self.serial += 1
        token = self.serial
        self.send(method, **{"@extra": token}, **fields)
        deadline = time.monotonic() + timeout
        while (remaining := deadline - time.monotonic()) > 0:
            reply = self.receive(min(1, remaining))
            if not reply or reply.get("@client_id") != self.client_id or reply.get("@extra") != token:
                continue
            if reply["@type"] == "error":
                raise TDError(method, reply["code"])
            return reply
        raise ReaderError(f"TDLib {method} timed out.")

    def start(self, directory, api_id, api_hash, *, files_directory=None):
        self.client_id = self.lib.td_create_client_id()
        auth = self.request("getAuthorizationState")["@type"]
        if auth != "authorizationStateWaitTdlibParameters":
            raise ReaderError("TDLib did not enter the expected initialization state.")
        require_type(self.request(
            "setTdlibParameters",
            use_test_dc=False,
            database_directory=str(directory),
            files_directory=str(files_directory or directory),
            database_encryption_key="",
            use_file_database=False,
            use_chat_info_database=False,
            use_message_database=False,
            use_secret_chats=False,
            api_id=api_id,
            api_hash=api_hash,
            system_language_code="ru",
            device_model="Telegram Chat Reader",
            system_version="macOS",
            application_version="1.0",
        ), "ok")
        self.wait(lambda: self.state.auth not in (None, auth))

    def __enter__(self):
        return self

    def __exit__(self, error_type, *_):
        if self.client_id is None or self.state.auth == "authorizationStateClosed":
            return
        try:
            self.send("close")
            self.wait(lambda: self.state.auth == "authorizationStateClosed", seconds=10,
                      failure="TDLib did not confirm session closure.")
        except ReaderError:
            if error_type is None:
                raise


def assert_private(st, mode, kind):
    if not kind(st.st_mode) or st.st_uid != os.getuid() or stat.S_IMODE(st.st_mode) != mode:
        raise ReaderError("Session directories must be owner-only 0700 and files owner-only 0600.")


def private_directory(path):
    path.mkdir(mode=0o700, parents=True, exist_ok=True)
    assert_private(path.lstat(), 0o700, stat.S_ISDIR)
    return path


def open_private(path, flags):
    fd = os.open(path, flags | os.O_NOFOLLOW, 0o600)
    try:
        assert_private(os.fstat(fd), 0o600, stat.S_ISREG)
    except BaseException:
        os.close(fd)
        raise
    return fd


def read_private_json(path):
    try:
        fd = open_private(path, os.O_RDONLY | os.O_NONBLOCK)
    except FileNotFoundError:
        return None
    with os.fdopen(fd, encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ReaderError("Invalid local session configuration.")
    return value


def write_private_json(path, value):
    fd, name = tempfile.mkstemp(dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(json_bytes(value))
        os.replace(name, path)
    finally:
        Path(name).unlink(missing_ok=True)


@contextmanager
def session_lock(root):
    with os.fdopen(open_private(root / "session.lock", os.O_CREAT | os.O_RDWR), "r+b") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise ReaderError("Another Telegram reader command is using the local session.") from error
        yield


def keychain_credentials(settings):
    if not isinstance(settings, dict):
        raise ReaderError("Invalid Keychain credentials configuration.")
    path = settings.get("path")
    account = settings.get("account")
    services = [settings.get("api_id_service"), settings.get("api_hash_service")]
    if not all(isinstance(value, str) and value for value in (path, account, *services)):
        raise ReaderError("Keychain path, account, and both item services are required.")
    if not Path(path).is_absolute():
        raise ReaderError("The configured Keychain path must be absolute.")
    values = []
    for service in services:
        try:
            found = subprocess.run(
                ["/usr/bin/security", "find-generic-password", "-a", account, "-s", service, "-w", path],
                stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                text=True, timeout=10, check=True,
            )
        except (subprocess.SubprocessError, OSError) as error:
            raise ReaderError("Could not read the configured Telegram items from macOS Keychain.") from error
        values.append(found.stdout.strip())
    return values


def configure_keychain(root):
    """Create references to user-entered items, resuming an interrupted first login."""
    if read_private_json(root / "credentials.json") is not None:
        return
    security = "/usr/bin/security"
    default = subprocess.run([security, "default-keychain", "-d", "user"],
                             capture_output=True, text=True)
    keychain = default.stdout.strip().strip('"')
    if default.returncode or not Path(keychain).is_absolute():
        raise ReaderError("Open Keychain Access and check the default user keychain.")
    account = getpass.getuser()
    settings = {"path": keychain, "account": account}
    print("Откройте https://my.telegram.org/apps в своём браузере. Если приложения ещё нет, "
          "создайте его в API development tools. Используйте api_id и api_hash со страницы "
          "своего приложения. Вводите их только здесь, в Terminal.", file=sys.stderr)
    for field in ("api_id", "api_hash"):
        service = f"telegram-chat-reader.{field}"
        settings[field + "_service"] = service
        item = ["-a", account, "-s", service]
        found = subprocess.run([security, "find-generic-password", *item, keychain],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if found.returncode == 0:
            continue
        if found.returncode != 44:  # errSecItemNotFound, truncated to a process exit status
            raise ReaderError("Could not inspect the default macOS keychain.")
        print(f"Введите {field} в запросе password от macOS и повторите для подтверждения.",
              file=sys.stderr, flush=True)
        # Trailing -w prompts on the terminal, keeping the value out of argv and shell history.
        if subprocess.run([security, "add-generic-password", *item, "-w"]).returncode:
            raise ReaderError("Could not save the item. Unlock your keychain and retry login.")
    write_private_json(root / "credentials.json", {"keychain": settings})


def credentials(root):
    config = read_private_json(root / "credentials.json")
    if not config or "keychain" not in config:
        raise ReaderError("Configure exact Telegram API items in macOS Keychain. See the skill setup.")
    api_id, api_hash = keychain_credentials(config["keychain"])
    if (not re.fullmatch(r"[0-9]{1,10}", api_id) or not 0 < int(api_id) < 2**31
            or not re.fullmatch(r"[0-9a-fA-F]{32}", api_hash)):
        raise ReaderError("Invalid Telegram API ID or hash in the configured Keychain items.")
    return int(api_id), api_hash


def hidden_input(prompt):
    with warnings.catch_warnings():
        warnings.simplefilter("error", getpass.GetPassWarning)
        try:
            return getpass.getpass(prompt)
        except getpass.GetPassWarning as error:
            raise ReaderError("The local terminal cannot securely hide input.") from error


def login(td):
    while td.state.auth != AUTH_READY:
        current = td.state.auth
        if current == "authorizationStateWaitPhoneNumber":
            phone = hidden_input("Telegram phone number, including country code: ")
            if not re.fullmatch(r"\+[1-9][0-9]{6,14}", phone):
                raise ReaderError("Enter the phone number in international format, without spaces.")
            td.request("setAuthenticationPhoneNumber", phone_number=phone, settings=None)
        elif current == "authorizationStateWaitCode":
            td.request("checkAuthenticationCode", code=hidden_input("Telegram login code: "))
        elif current == "authorizationStateWaitEmailAddress":
            td.request("setAuthenticationEmailAddress", email_address=hidden_input("Telegram login email: "))
        elif current == "authorizationStateWaitEmailCode":
            td.request("checkAuthenticationEmailCode", code={
                "@type": "emailAddressAuthenticationCode",
                "code": hidden_input("Telegram email code: "),
            })
        elif current == "authorizationStateWaitPassword":
            td.request("checkAuthenticationPassword", password=hidden_input("Telegram two-step password: "))
        else:
            raise ReaderError("Telegram requested an unsupported authorization step.")
        td.wait(lambda: td.state.auth != current, failure="Telegram did not confirm the login step.")


def bind_account(td, root, *, interactive):
    path = root / "account.json"
    account = read_private_json(path)
    me = require_type(td.request("getMe"), "user")
    if me["type"]["@type"] != "userTypeRegular" or type(me["id"]) is not int or me["id"] <= 0:
        raise ReaderError("Telegram did not return a regular user account.")
    if account is None and interactive:
        write_private_json(path, {"user_id": me["id"]})
    elif account != {"user_id": me["id"]}:
        raise ReaderError("The Telegram session does not match the locally bound account.")


def selector_key(selector):
    if re.fullmatch(r"-?[0-9]{1,16}", selector):
        return "id", int(selector)
    if match := re.fullmatch(r"@([A-Za-z][A-Za-z0-9_]{0,31})", selector):
        return "username", match[1].lower()
    if match := re.fullmatch(r"https://t\.me/c/([0-9]{1,16})/[0-9]+", selector):
        return "supergroup", int(match[1])
    if match := re.fullmatch(r"https://t\.me/([A-Za-z][A-Za-z0-9_]{0,31})(?:/[0-9]+)?/?", selector):
        return "username", match[1].lower()
    if selector.startswith("@") or "://" in selector:
        raise ReaderError("Unsupported Telegram selector. Use an exact title or TDLib chat ID.")
    return "title", selector


def chat_summary(chat):
    return {"id": chat["id"], "title": chat["title"], "type": chat["type"]["@type"]}


class Scope:
    def __init__(self, td, folder, *, private_only=False):
        self.td = td
        self.folder = folder
        self.private_only = private_only
        self.explicit_chat_id = None
        self.folder_id = self.exact_folder() if folder is not None else None
        self.revision = td.state.connection_revision
        if self.folder_id is None:
            lists = [{"@type": "chatListMain"}, {"@type": "chatListArchive"}]
        else:
            lists = [{"@type": "chatListFolder", "chat_folder_id": self.folder_id}]
        self.lists = {list_key(item) for item in lists}
        self.guard()
        if self.folder_id is not None:
            detail = require_type(td.request("getChatFolder", chat_folder_id=self.folder_id), "chatFolder")
            if folder_title(detail) != self.folder:
                raise ReaderError("The Telegram folder changed during selection.")
        for chat_list in lists:
            self.load(chat_list)
        self.guard()

    def exact_folder(self):
        matches = [folder_id for folder_id, name in (self.td.state.folders or ()) if name == self.folder]
        if len(matches) != 1:
            raise ReaderError("The exact Telegram folder is missing or ambiguous.")
        return matches[0]

    def load(self, chat_list):
        for _ in range(100):
            self.guard()
            try:
                require_type(self.td.request("loadChats", chat_list=chat_list, limit=100), "ok")
            except TDError as error:
                # TDLib explicitly signals list exhaustion via 404.
                if error.code == 404:
                    return
                raise
        raise ReaderError("Telegram did not confirm the end of the chat list.")

    def guard(self, chat_id=None):
        self.td.drain()
        state = self.td.state
        if (state.auth != AUTH_READY or state.connection != CONNECTED
                or state.connection_revision != self.revision):
            raise ReaderError("Telegram connection or authorization changed. Retry after synchronization.")
        if self.folder_id is not None and self.exact_folder() != self.folder_id:
            raise ReaderError("The Telegram folder changed during selection.")
        if chat_id is not None:
            self.require_member(state.chats.get(chat_id))

    def require_member(self, chat):
        if chat is None or not (
            chat["lists"] & self.lists or
            (self.folder_id is None and chat["id"] == self.explicit_chat_id)
        ):
            raise ReaderError("Current Telegram membership in the selected chat list is unproven.")
        if self.private_only and chat["type"]["@type"] != "chatTypePrivate":
            raise ReaderError("The selected Telegram chat is not a private dialog.")
        if chat["protected"] or chat["type"]["@type"] == "chatTypeSecret":
            raise ReaderError("The selected Telegram chat has protected or secret content.")

    def candidates(self):
        return [chat for chat in self.td.state.chats.values() if chat["lists"] & self.lists]

    def usernames(self, chat):
        kind = chat["type"]
        if kind["@type"] == "chatTypePrivate":
            return self.td.state.users.get(kind["user_id"], (None, ()))[1]
        if kind["@type"] == "chatTypeSupergroup":
            return self.td.state.supergroups.get(kind["supergroup_id"], ())
        return ()

    def resolve(self, selector):
        kind, value = selector_key(selector)
        self.guard()
        matches = []
        for chat in self.candidates():
            if self.private_only and chat["type"]["@type"] != "chatTypePrivate":
                continue
            if kind == "username":
                matched = value in self.usernames(chat)
            elif kind == "supergroup":
                matched = value == chat["type"].get("supergroup_id")
            else:
                matched = value == chat[kind]
            if matched:
                matches.append(chat)
        if not matches and kind == "username" and self.folder_id is None and not self.private_only:
            result = require_type(self.td.request("searchPublicChat", username=value), "chat")
            selected = chat_metadata(result)
            self.explicit_chat_id = selected["id"]
            self.td.state.chats.setdefault(selected["id"], selected)
            self.require_member(selected)
            self.guard(selected["id"])
            return selected
        if len(matches) != 1:
            raise ReaderError("The exact chat selector is missing or ambiguous in the allowed chat list.")
        self.require_member(matches[0])
        return matches[0]

    @contextmanager
    def verified_chat(self, chat_id):
        self.guard(chat_id)
        chat = require_type(self.td.request("getChat", chat_id=chat_id), "chat")
        if chat["id"] != chat_id:
            raise ReaderError("TDLib returned a different chat during scope verification.")
        self.require_member(chat_metadata(chat))
        self.guard(chat_id)
        try:
            yield
        finally:
            self.guard(chat_id)

    def read(self, chat_id, method, **fields):
        with self.verified_chat(chat_id):
            return self.td.request(method, chat_id=chat_id, **fields)

    def download(self, chat_id, file_id, byte_limit, *, timeout=150):
        with self.verified_chat(chat_id):
            return self.td.request("downloadFile", timeout=timeout, file_id=file_id,
                                   priority=16, offset=0, limit=byte_limit, synchronous=True)


def utc(epoch):
    return datetime.fromtimestamp(epoch, timezone.utc).isoformat().replace("+00:00", "Z")


def message_record(state, message, chat_id, kind, text):
    sender = message["sender_id"]
    if sender["@type"] == "messageSenderUser":
        author_id = sender["user_id"]
        author_type = "user"
        author_name = state.users.get(author_id, (None, ()))[0]
    elif sender["@type"] == "messageSenderChat":
        author_id = sender["chat_id"]
        author_type = "chat"
        author_name = state.chats.get(author_id, {}).get("title")
    else:
        raise ReaderError("TDLib returned an unsupported message sender schema.")
    return {
        "chat_id": chat_id,
        "message_id": message["id"],
        "date": utc(message["date"]),
        "author": {"type": author_type, "id": author_id, "name": message.get("author_signature") or author_name},
        "text": text,
        "type": kind,
    }


def content_metadata(value):
    if isinstance(value, list):
        return [content_metadata(item) for item in value]
    if not isinstance(value, dict):
        return value
    if value.get("@type") == "file":
        return {
            "size": value.get("size") or value.get("expected_size"),
            "can_download": (value.get("local") or {}).get("can_be_downloaded") is True,
        }
    return {
        key: content_metadata(item) for key, item in value.items()
        if key not in {"minithumbnail", "thumbnail", "waveform"}
    }


def is_savable(message):
    return message.get("can_be_saved") is True and not message.get("self_destruct_type")


def history_record(state, message, *, all_types):
    content = message["content"]
    kind = content["@type"]
    field = "text" if kind == "messageText" else "caption"
    text = (content.get(field) or {}).get("text")
    if (not all_types and not text) or message.get("sending_state") is not None:
        return None, False
    if not is_savable(message):
        return None, True
    record = message_record(state, message, message["chat_id"], kind, text)
    if all_types:
        record["content"] = content_metadata(content)
    return record, False


def history(scope, selector, since, until, limit, *, all_types=False):
    chat = scope.resolve(selector)
    chat_id = chat["id"]
    state = scope.td.state
    seen = set()
    records = []
    omitted_protected = 0
    cursor = 0
    stalled = 0
    reason = "page_budget"
    anchor = None
    if until is not None:
        try:
            anchor = require_type(scope.read(chat_id, "getChatMessageByDate", date=until - 1), "message")
        except TDError as error:
            if error.code != 404:
                raise
            reason = "end_of_history"
        else:
            if anchor["chat_id"] != chat_id or not 0 < anchor["id"] or anchor["date"] >= until:
                raise ReaderError("TDLib returned an invalid history date anchor.")
    page_budget = MAX_PAGES + (anchor is not None) if reason == "page_budget" else 0
    for page_number in range(page_budget):
        if page_number == 0 and anchor is not None:
            # Current TDLib can exclude from_message_id from the response.
            # Preserve the date anchor itself and deduplicate it on subsequent pages.
            page = [anchor]
        else:
            response = require_type(scope.read(
                chat_id, "getChatHistory", from_message_id=cursor, offset=0,
                limit=min(100, limit + 2), only_local=False,
            ), "messages")
            page = response["messages"]
        if not page:
            reason = "end_of_history"
            break
        oldest = cursor
        for message in page:
            message_id = message["id"]
            date = message["date"]
            if (message["chat_id"] != chat_id or message_id <= 0 or date < 0
                    or (cursor and message_id > cursor)):
                raise ReaderError("TDLib returned a message outside the verified chat or cursor.")
            oldest = min(oldest, message_id) if oldest else message_id
            if message_id in seen:
                continue
            seen.add(message_id)
            if until is not None and date >= until:
                continue
            if date < since:
                reason = "since_reached"
                break
            record, protected = history_record(state, message, all_types=all_types)
            if protected:
                omitted_protected += 1
            if record is None:
                continue
            if len(records) == limit:
                reason = "limit"
                break
            records.append((date, message_id, record))
        if reason != "page_budget":
            break
        if oldest == cursor:
            stalled += 1
            if stalled >= 3:
                reason = "pagination_stalled"
                break
        else:
            cursor = oldest
            stalled = 0

    scope.guard(chat_id)
    return {
        "chat": chat_summary(chat),
        "folder": scope.folder,
        "folder_id": scope.folder_id,
        "since": utc(since),
        "until": utc(until) if until is not None else None,
        "complete": reason in ("since_reached", "end_of_history") and omitted_protected == 0,
        "stop_reason": reason,
        "omitted_protected": omitted_protected,
        "messages": [record for _, _, record in sorted(records)],
    }


def fetch_media(scope, chat_id, message_id):
    message = require_type(scope.read(chat_id, "getMessage", message_id=message_id), "message")
    if (message["chat_id"] != chat_id or message["id"] != message_id
            or message.get("sending_state") is not None or not is_savable(message)):
        raise ReaderError("The selected message cannot be saved or verified.")
    return message


def media_file(message):
    content = message["content"]
    kind = content["@type"]
    if kind == "messagePhoto":
        sizes = [size for size in content["photo"]["sizes"]
                 if size.get("photo") and (size["photo"].get("local") or {}).get("can_be_downloaded") is not False]
        if not sizes:
            raise ReaderError("Telegram did not provide a downloadable photo.")
        largest = max(sizes, key=lambda size: size["width"] * size["height"])
        return require_type(largest["photo"], "file"), ".jpg"
    if kind not in MEDIA_FIELDS:
        raise ReaderError("This message type has no supported downloadable attachment.")
    container, field, suffix = MEDIA_FIELDS[kind]
    attachment = content[container]
    extension = Path(attachment.get("file_name") or "").suffix.lower()
    if re.fullmatch(r"\.[a-z0-9]{1,12}", extension):
        suffix = extension
    if kind == "messageSticker":
        suffix = {"stickerFormatTgs": ".tgs", "stickerFormatWebm": ".webm"}.get(
            (attachment.get("format") or {}).get("@type"), suffix)
    return require_type(attachment[field], "file"), suffix


def media_path(scope, chat_id, message_id, cache, file, *, maximum_bytes=MAX_MEDIA_BYTES):
    file_id = file["id"]
    if not isinstance(file_id, int) or file_id <= 0:
        raise ReaderError("Telegram did not provide a valid attachment ID.")
    size = max(file.get("size", 0), file.get("expected_size", 0))
    if maximum_bytes is not None and size > maximum_bytes:
        raise ReaderError("This attachment exceeds the 100 MiB download limit.")
    if maximum_bytes is None:
        timeout = min(3600, max(150, (size or 256 * 1024 * 1024) // (256 * 1024) + 90))
        reply = scope.download(chat_id, file_id, 0, timeout=timeout)
    else:
        reply = scope.download(chat_id, file_id, maximum_bytes + 1)
    downloaded = require_type(reply, "file")
    local = downloaded["local"]
    if downloaded["id"] != file_id or not local["is_downloading_completed"] or not local["path"]:
        raise ReaderError("Telegram did not complete the attachment download.")
    path = Path(local["path"]).resolve(strict=True)
    if not path.is_relative_to(cache.resolve()) or not path.is_file():
        raise ReaderError("Telegram returned an attachment outside the private temporary directory.")
    actual_size = path.stat().st_size
    if not actual_size or (maximum_bytes is not None and actual_size > maximum_bytes):
        raise ReaderError("Downloaded attachment is empty or exceeds the requested limit.")
    if media_file(fetch_media(scope, chat_id, message_id))[0]["id"] != file_id:
        raise ReaderError("The selected attachment changed during download.")
    return path


def extract_text(path, kind, suffix):
    if kind == "messagePhoto" or suffix in {".pdf", ".png", ".jpg", ".jpeg", ".heic", ".tiff", ".webp"}:
        mode = "pdf" if suffix == ".pdf" else "photo"
        helper = Path(__file__).with_name("extract_text.swift")
        result = subprocess.run(["/usr/bin/swift", str(helper), mode, str(path)],
                                capture_output=True, timeout=90, check=True)
        text = result.stdout.decode("utf-8")
    elif suffix in {".txt", ".csv", ".tsv", ".md", ".json", ".log", ".srt", ".vtt"}:
        limit = 4 * (MAX_EXTRACTED_CHARS + 1)
        with path.open("rb") as stream:
            data = stream.read(limit + 1)
        encoding = "utf-16" if data.startswith((b"\xff\xfe", b"\xfe\xff")) else "utf-8-sig"
        text = codecs.getincrementaldecoder(encoding)().decode(data[:limit], final=len(data) <= limit)
    elif suffix == ".docx":
        with zipfile.ZipFile(path) as document:
            with document.open("word/document.xml") as xml:
                data = xml.read(8 * 1024 * 1024 + 1)
        if len(data) > 8 * 1024 * 1024 or b"<!DOCTYPE" in data.upper():
            raise ValueError("Unsupported DOCX XML")
        root = ElementTree.fromstring(data)
        ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
        text = "\n".join("".join(node.text or "" for node in paragraph.iter(f"{ns}t"))
                         for paragraph in root.iter(f"{ns}p"))
    else:
        return {"status": "unsupported_format"}
    return {"status": "ok" if text.strip() else "no_text", "text": text[:MAX_EXTRACTED_CHARS],
            "truncated": len(text) > MAX_EXTRACTED_CHARS}


def export_media(scope, chat_id, message_id, cache, args):
    message = fetch_media(scope, chat_id, message_id)
    file, suffix = media_file(message)
    source = media_path(scope, chat_id, message_id, cache, file)
    kind = message["content"]["@type"]
    result = {"chat_id": chat_id, "message_id": message_id, "type": kind}
    if args.extract_text:
        try:
            result["extraction"] = extract_text(source, kind, suffix)
        except (OSError, ValueError, subprocess.SubprocessError, zipfile.BadZipFile, KeyError, ElementTree.ParseError):
            result["extraction"] = {"status": "failed"}
        if media_file(fetch_media(scope, chat_id, message_id))[0]["id"] != file["id"]:
            raise ReaderError("The selected attachment changed during text extraction.")
    directory = private_directory(args.output_dir)
    target = directory / f"{chat_id}-{message_id}{suffix}"
    try:
        fd = open_private(target, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as error:
        raise ReaderError("The target attachment already exists. Use a different output directory.") from error
    try:
        with os.fdopen(fd, "wb") as output, source.open("rb") as input_file:
            shutil.copyfileobj(input_file, output)
        scope.guard(chat_id)
    except BaseException:
        target.unlink(missing_ok=True)
        raise
    return {**result, "path": str(target.absolute()), "bytes": target.stat().st_size}


def local_transcript(source, directory, model, language, *, duration=0):
    wav = directory / "speech.wav"
    prefix = directory / "speech"
    try:
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-protocol_whitelist", "file",
                        "-format_whitelist", MEDIA_DEMUXERS,
                        "-i", str(source), "-map", "0:a:0", "-ac", "1", "-ar", "16000",
                        "-c:a", "pcm_s16le", str(wav)], capture_output=True,
                       timeout=max(90, duration // 4 + 60), check=True)
        subprocess.run(["whisper-cli", "-m", str(model), "-f", str(wav), "-l", language,
                        "-nt", "-otxt", "-of", str(prefix)], capture_output=True,
                       timeout=max(180, duration + 120), check=True)
        return prefix.with_suffix(".txt").read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError, subprocess.SubprocessError) as error:
        raise ReaderError("Local transcription failed while decoding audio or running Whisper.") from error


def saved_transcript(content):
    container = {"messageVoiceNote": "voice_note", "messageVideoNote": "video_note"}.get(content["@type"])
    if container:
        response = content[container].get("speech_recognition_result") or {}
        if response.get("@type") == "speechRecognitionResultText" and response.get("text"):
            return {"source": "telegram", "text": response["text"]}
    return None


def analyze_attachment(source, content, suffix, work_dir):
    kind = content["@type"]
    if ready := saved_transcript(content):
        return {"status": "ok", "transcription": ready}
    mime = (content.get("document") or {}).get("mime_type") or ""
    is_audio_video = (kind in {"messageVoiceNote", "messageVideoNote", "messageAudio", "messageVideo", "messageAnimation"}
                      or mime.startswith(("audio/", "video/"))
                      or suffix in {".mp4", ".m4a", ".ogg", ".opus", ".wav", ".mp3", ".mov", ".webm", ".mkv", ".aac", ".flac"})
    if is_audio_video:
        if not shutil.which("ffprobe") or not shutil.which("ffmpeg"):
            return {"status": "missing_dependencies"}
        try:
            tracks = subprocess.run(["ffprobe", "-v", "error", "-protocol_whitelist", "file",
                                     "-format_whitelist", MEDIA_DEMUXERS, "-select_streams", "a",
                                     "-show_entries", "stream=index:format=duration",
                                     "-of", "json", str(source)], capture_output=True, timeout=45, check=True)
            probe = json.loads(tracks.stdout)
            if not probe.get("streams"):
                return {"status": "no_audio"}
            if not DEFAULT_MODEL.is_file() or not shutil.which("whisper-cli"):
                return {"status": "missing_dependencies"}
            raw_duration = (probe.get("format") or {}).get("duration")
            duration = int(float(raw_duration)) if raw_duration not in (None, "N/A") else 0
            text = local_transcript(source, work_dir, DEFAULT_MODEL, "auto", duration=duration)
        except (ReaderError, OSError, ValueError, OverflowError, subprocess.SubprocessError):
            return {"status": "processing_failed"}
        return {"status": "ok" if text else "no_speech",
                "transcription": {"source": "local_whisper", "text": text}}
    try:
        return extract_text(source, kind, suffix)
    except (OSError, ValueError, subprocess.SubprocessError, zipfile.BadZipFile, KeyError, ElementTree.ParseError):
        return {"status": "processing_failed"}


def transcribe(scope, chat_id, message_id, cache, args):
    message = fetch_media(scope, chat_id, message_id)
    content = message["content"]
    kind = content["@type"]
    if kind not in {"messageVoiceNote", "messageVideoNote"}:
        raise ReaderError("Transcription requires a voice note or a video note.")
    result = {"chat_id": chat_id, "message_id": message_id, "type": kind}
    if ready := saved_transcript(content):
        return {**result, **ready}
    model = args.model or DEFAULT_MODEL
    if not model.is_file() or not shutil.which("whisper-cli") or not shutil.which("ffmpeg"):
        raise ReaderError("Local transcription needs FFmpeg, whisper-cli and a Whisper model. See the skill setup.")
    file, _ = media_file(message)
    path = media_path(scope, chat_id, message_id, cache, file)
    text = local_transcript(path, cache, model, args.language)
    if media_file(fetch_media(scope, chat_id, message_id))[0]["id"] != file["id"]:
        raise ReaderError("The selected attachment changed during transcription.")
    return {**result, "source": "local_whisper", "text": text}


def timestamp(value):
    try:
        date = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if date.utcoffset() is None or date.microsecond:
            raise ValueError
        epoch = int(date.timestamp())
        if not 1 < epoch < 2**31:
            raise ValueError
        return epoch
    except (ValueError, OverflowError, OSError) as error:
        raise argparse.ArgumentTypeError("use an ISO 8601 time with UTC offset and whole seconds") from error


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("login", help="authorize a local Telegram user in an interactive terminal")
    commands.add_parser("status", help="check the existing session without requesting login")
    chats = commands.add_parser("chats", help="list chats in one exact folder")
    chats.add_argument("--folder", required=True)
    read = commands.add_parser("history", help="read bounded history of one exact chat")
    media = commands.add_parser("media", help="download the attachment of one verified message")
    speech = commands.add_parser("transcribe", help="read or locally transcribe one voice or video note")
    for command in (read, media, speech):
        command.add_argument("--chat", required=True)
        command.add_argument("--folder")
        command.add_argument("--private-only", action="store_true", help="only read an existing private dialog")
    for command in (media, speech):
        command.add_argument("--message-id", type=int, required=True, help="TDLib message ID from history")
    read.add_argument("--since", type=timestamp, help="inclusive ISO 8601 time")
    read.add_argument("--until", type=timestamp, help="exclusive ISO 8601 time")
    read.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    read.add_argument("--all-types", action="store_true", help="include messages without text or caption")
    media.add_argument("--output-dir", type=Path, required=True, help="owner-only directory for the attachment")
    media.add_argument("--extract-text", action="store_true", help="read photo, PDF, DOCX or TXT text locally")
    speech.add_argument("--language", default="auto", help="Whisper language code, for example ru")
    speech.add_argument("--model", type=Path, help="path to a local multilingual Whisper model")
    args = parser.parse_args(argv)
    if hasattr(args, "chat") and not args.chat.strip():
        parser.error("--chat must be a nonempty exact selector")
    if hasattr(args, "message_id") and not 0 < args.message_id < 2**53:
        parser.error("--message-id must be a positive TDLib message ID")
    if args.command == "transcribe" and not re.fullmatch(r"auto|[a-z]{2,3}", args.language):
        parser.error("--language must be auto or a lowercase language code")
    if args.command == "history":
        if not 1 <= args.limit <= MAX_LIMIT:
            parser.error(f"history requires --limit from 1 to {MAX_LIMIT}")
        if args.since is None:
            args.since = max(1, (args.until or int(time.time())) - WEEK)
        if args.until is not None and args.until <= args.since:
            parser.error("--until must be later than --since")
    if getattr(args, "folder", None) is not None and not args.folder.strip():
        parser.error("--folder must be a nonempty exact title")
    return args


def run(args):
    interactive = args.command == "login"
    if interactive and not sys.stdin.isatty():
        raise ReaderError("Run login in a local interactive Terminal.")
    if not STATE_DIR.exists() and not interactive:
        if args.command == "status":
            return {"authorized": False, "reason": "login_required"}
        raise ReaderError("A bound Telegram session is required. Run login in a local Terminal.")

    root = private_directory(STATE_DIR)
    with session_lock(root):
        if not interactive and read_private_json(root / "account.json") is None:
            if args.command == "status":
                return {"authorized": False, "reason": "login_required"}
            raise ReaderError("A bound Telegram session is required. Run login in a local Terminal.")
        use_cache = args.command in ("media", "transcribe")
        temporary = tempfile.TemporaryDirectory(prefix="media-", dir=root) if use_cache else nullcontext()
        with temporary as temporary_path, TDLib() as td:
            cache = Path(temporary_path).resolve() if temporary_path else None
            if interactive:
                configure_keychain(root)
            td.start(private_directory(root / "tdlib"), *credentials(root), files_directory=cache)
            if interactive:
                login(td)
            if td.state.auth != AUTH_READY:
                if args.command == "status":
                    return {"authorized": False, "reason": "login_required", "tdlib_version": td.version}
                raise ReaderError("Telegram authorization is required. Run login in a local Terminal.")
            bind_account(td, root, interactive=interactive)
            if args.command in ("login", "status"):
                return {"authorized": True, "tdlib_version": td.version}
            td.wait(lambda: td.state.connection == CONNECTED and (args.folder is None or td.state.folders is not None),
                    seconds=40, failure="Telegram did not confirm synchronization and folder state.")
            scope = Scope(td, args.folder, private_only=getattr(args, "private_only", False))
            if args.command == "chats":
                return {
                    "folder": scope.folder,
                    "folder_id": scope.folder_id,
                    "chats": [chat_summary(chat) for chat in sorted(scope.candidates(), key=lambda c: (c["title"], c["id"]))],
                }
            if args.command == "history":
                return history(scope, args.chat, args.since, args.until, args.limit, all_types=args.all_types)
            chat_id = scope.resolve(args.chat)["id"]
            if args.command == "media":
                return export_media(scope, chat_id, args.message_id, cache, args)
            return transcribe(scope, chat_id, args.message_id, cache, args)


def main():
    args = parse_args()
    os.umask(0o077)
    try:
        result = run(args)
    except ReaderError as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print('{"error": "Telegram reader interrupted."}', file=sys.stderr)
        return 130
    except (OSError, ValueError, KeyError, TypeError, EOFError):
        # Exception payloads may include TDLib data, keychain output or paths.
        print('{"error": "Local configuration or TDLib response could not be read."}', file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
