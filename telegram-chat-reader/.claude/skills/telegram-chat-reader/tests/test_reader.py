import json
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import reader


FOLDER = {"@type": "chatListFolder", "chat_folder_id": 9}


def folder_info(number, name="02 Работа"):
    return {"id": number, "name": {"text": {"text": name}}}


def chat(chat_id, title, *, member=True):
    return {
        "@type": "chat", "id": chat_id, "title": title,
        "type": {"@type": "chatTypePrivate", "user_id": chat_id},
        "chat_lists": [FOLDER] if member else [],
        # An unrelated position does not establish membership.
        "positions": [{"list": FOLDER, "order": "1"}] if not member else [],
        "has_protected_content": False,
    }


def message(message_id, date, text="текст", *, kind="messageText", saved=True):
    return {
        "id": message_id, "chat_id": 11, "date": date,
        "can_be_saved": saved, "sender_id": {"@type": "messageSenderUser", "user_id": 31},
        "content": {"@type": kind, ("text" if kind == "messageText" else "caption"): {"text": text}},
    }


class FakeTDLib:
    def __init__(self, chats, pages=(), *, folders=None, connection="connectionStateReady"):
        self.state = reader.State()
        self.state.apply({"@type": "updateAuthorizationState", "authorization_state": {
            "@type": "authorizationStateReady",
        }})
        self.state.apply({"@type": "updateConnectionState", "state": {"@type": connection}})
        self.state.apply({"@type": "updateChatFolders", "chat_folders": folders or [folder_info(9)]})
        self.chats = {entry["id"]: entry for entry in chats}
        self.pages = iter(pages)
        self.calls = []
        self.loads = 0
        self.after_history = lambda: None

    def drain(self):
        pass

    def request(self, method, **fields):
        self.calls.append((method, fields))
        if method == "getChatFolder":
            return {"@type": "chatFolder", "name": {"text": {"text": "02 Работа"}}}
        if method == "loadChats":
            self.loads += 1
            if self.loads > len(self.chats):
                raise reader.TDError(method, 404)
            entry = list(self.chats.values())[self.loads - 1]
            self.state.apply({"@type": "updateNewChat", "chat": entry})
            return {"@type": "ok"}
        if method == "getChat":
            return self.chats[fields["chat_id"]]
        if method == "getChatMessageByDate":
            return next(self.pages)
        if method == "getChatHistory":
            result = next(self.pages)
            self.after_history()
            return {"@type": "messages", "total_count": -1, "messages": result}
        raise AssertionError(method)


class ReaderTests(unittest.TestCase):
    def history(self, td, selector="Целевой", since=100, until=None, limit=10):
        scope = reader.Scope(td, "02 Работа")
        return reader.history(scope, selector, since, until, limit)

    def assert_no_history(self, td):
        self.assertFalse(any(method in {"getChatMessageByDate", "getChatHistory"}
                             for method, _ in td.calls))

    def test_rejects_id_and_title_outside_folder_even_with_nonzero_position(self):
        for selector in ("22", "Чужой", "https://t.me/outside_chat/42"):
            with self.subTest(selector=selector):
                td = FakeTDLib([chat(11, "Целевой"), chat(22, "Чужой", member=False)])
                td.state.apply({"@type": "updateUser", "user": {"id": 22, "usernames": {
                    "active_usernames": ["outside_chat"],
                }}})
                with self.assertRaises(reader.ReaderError):
                    self.history(td, selector, until=200)
                self.assert_no_history(td)

    def test_exact_duplicate_title_or_folder_stops_before_history(self):
        for td in (
            FakeTDLib([chat(11, "Целевой"), chat(22, "Целевой")]),
            FakeTDLib([chat(11, "Целевой")], folders=[folder_info(9), folder_info(10)]),
        ):
            with self.assertRaises(reader.ReaderError):
                self.history(td)
            self.assert_no_history(td)

    def test_disconnected_and_membership_changed_after_load_fail_closed(self):
        for connection in ("connectionStateUpdating", "connectionStateReady"):
            td = FakeTDLib([chat(11, "Целевой")], connection=connection)
            original = td.request

            def request(method, **fields):
                if method == "getChat":
                    return chat(11, "Целевой", member=False)
                return original(method, **fields)

            td.request = request
            with self.assertRaises(reader.ReaderError):
                self.history(td)
            self.assert_no_history(td)

    def test_revocation_mid_page_discards_output_and_stops(self):
        td = FakeTDLib([chat(11, "Целевой")], pages=[[message(30, 145)]])
        td.after_history = lambda: td.state.apply({
            "@type": "updateChatRemovedFromList", "chat_id": 11, "chat_list": FOLDER,
        })
        with self.assertRaises(reader.ReaderError):
            self.history(td)
        self.assertEqual(sum(method == "getChatHistory" for method, _ in td.calls), 1)

    def test_older_pages_continue_after_short_page_and_deduplicate(self):
        td = FakeTDLib([chat(11, "Целевой")], pages=[
            [message(30, 145), message(29, 144, "описание", kind="messagePhoto")],
            [message(29, 144), message(26, 100), message(25, 99)],
        ])
        td.state.apply({"@type": "updateUser", "user": {"id": 31, "first_name": "Анна", "last_name": "И."}})
        result = self.history(td)
        self.assertTrue(result["complete"])
        self.assertEqual([m["message_id"] for m in result["messages"]], [26, 29, 30])
        self.assertEqual(result["messages"][1]["text"], "описание")
        self.assertEqual(result["messages"][1]["author"], {"type": "user", "id": 31, "name": "Анна И."})
        self.assertEqual([f["from_message_id"] for m, f in td.calls if m == "getChatHistory"], [0, 29])

    def test_limit_requires_proof_of_additional_in_range_message(self):
        td = FakeTDLib([chat(11, "Целевой")], pages=[
            [message(30, 145), message(29, 144), message(28, 143)],
        ])
        result = self.history(td, limit=2)
        self.assertFalse(result["complete"])
        self.assertEqual(result["stop_reason"], "limit")
        self.assertEqual([m["message_id"] for m in result["messages"]], [29, 30])

    def test_inclusive_repeated_cursor_cannot_prove_completeness(self):
        td = FakeTDLib([chat(11, "Целевой")], pages=[[message(30, 145)]] * 4)
        result = self.history(td)
        self.assertFalse(result["complete"])
        self.assertEqual(result["stop_reason"], "pagination_stalled")
        self.assertEqual(len(result["messages"]), 1)

    def test_until_seeks_to_last_included_second_before_history(self):
        td = FakeTDLib([chat(11, "Целевой")], pages=[
            {"@type": "message", **message(30, 149)}, [message(25, 99)],
        ])
        result = self.history(td, until=150)
        self.assertTrue(result["complete"])
        self.assertEqual(td.calls[4], ("getChatMessageByDate", {"chat_id": 11, "date": 149}))
        self.assertEqual([m["message_id"] for m in result["messages"]], [30])

    def test_exact_username_and_message_link_resolve_inside_folder(self):
        for selector in ("@target_1", "https://t.me/target_1/42"):
            td = FakeTDLib([chat(11, "Целевой")], pages=[[]])
            td.state.apply({"@type": "updateUser", "user": {"id": 11, "usernames": {
                "active_usernames": ["target_1"], "disabled_usernames": ["someone_else"],
            }}})
            self.assertEqual(self.history(td, selector)["chat"]["id"], 11)

    def test_exact_public_link_outside_dialogs_is_resolved_only_without_folder(self):
        for folder in (None, "02 Работа"):
            with self.subTest(folder=folder):
                target = chat(11, "Публичный", member=False)
                td = FakeTDLib([target], pages=[[message(30, 145), message(25, 99)]])
                original = td.request

                def request(method, **fields):
                    if method == "searchPublicChat":
                        td.calls.append((method, fields))
                        return target
                    return original(method, **fields)

                td.request = request
                scope = reader.Scope(td, folder)
                link = "https://t.me/target_1/42"
                if folder is None:
                    result = reader.history(scope, link, 100, None, 10)
                    self.assertEqual(result["chat"]["id"], 11)
                    self.assertEqual(len(result["messages"]), 1)
                    self.assertIn(("searchPublicChat", {"username": "target_1"}), td.calls)
                else:
                    with self.assertRaises(reader.ReaderError):
                        reader.history(scope, link, 100, None, 10)
                    self.assert_no_history(td)
                    self.assertFalse(any(method == "searchPublicChat" for method, _ in td.calls))

    def test_protected_messages_are_omitted_with_explicit_gap(self):
        td = FakeTDLib([chat(11, "Целевой")], pages=[
            [message(30, 145, "protected", saved=False), message(25, 99)],
        ])
        result = self.history(td)
        self.assertFalse(result["complete"])
        self.assertEqual(result["omitted_protected"], 1)
        self.assertEqual(result["messages"], [])


class LocalSessionTests(unittest.TestCase):
    @unittest.skipUnless(sys.platform == 'darwin', 'macOS Keychain')
    def test_first_login_resumes_after_one_keychain_item_was_created(self):
        keychain = "/example/user.keychain-db"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(reader.subprocess, "run") as run:
                run.side_effect = [
                    reader.subprocess.CompletedProcess([], 0, stdout=f'    "{keychain}"\n'),
                    reader.subprocess.CompletedProcess([], 0),
                    reader.subprocess.CompletedProcess([], 44),
                    reader.subprocess.CompletedProcess([], 0),
                ]
                reader.configure_keychain(root)
                commands = [call.args[0] for call in run.call_args_list]
                self.assertEqual([cmd[1] for cmd in commands], [
                    "default-keychain", "find-generic-password",
                    "find-generic-password", "add-generic-password",
                ])
                self.assertEqual(commands[-1][-2:], ["telegram-chat-reader.api_hash", "-w"])
                reader.configure_keychain(root)
                self.assertEqual(run.call_count, 4)
            config = reader.read_private_json(root / "credentials.json")["keychain"]
            self.assertEqual(config["path"], keychain)
            self.assertEqual(config["api_hash_service"], "telegram-chat-reader.api_hash")

    @unittest.skipUnless(sys.platform == 'darwin', 'macOS Keychain')
    def test_keychain_failure_does_not_create_configuration(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(reader.subprocess, "run") as run:
                run.side_effect = [
                    reader.subprocess.CompletedProcess([], 0, stdout='"/example/user.keychain-db"'),
                    reader.subprocess.CompletedProcess([], 44),
                    reader.subprocess.CompletedProcess([], 1),
                ]
                with self.assertRaises(reader.ReaderError):
                    reader.configure_keychain(root)
            self.assertFalse((root / "credentials.json").exists())

    def test_unbound_status_does_not_open_a_tdlib_client(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(reader, "STATE_DIR", Path(directory) / "fresh"), patch.object(reader, "TDLib") as tdlib:
                result = reader.run(reader.parse_args(["status"]))
                self.assertEqual(result, {"authorized": False, "reason": "login_required"})
                tdlib.assert_not_called()

    @unittest.skipUnless(sys.platform == 'darwin', 'macOS Keychain')
    def test_keychain_uses_exact_items_and_leaves_reference_file_unchanged(self):
        config = {"keychain": {
            "path": "/path/to/telegram.keychain-db",
            "account": "test-owner",
            "api_id_service": "test-id",
            "api_hash_service": "test-hash",
        }}
        secret = "a" * 32
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "credentials.json"
            reader.write_private_json(path, config)
            with patch.object(reader.subprocess, "run") as run:
                run.side_effect = [
                    reader.subprocess.CompletedProcess([], 0, stdout="123"),
                    reader.subprocess.CompletedProcess([], 0, stdout=secret),
                ]
                self.assertEqual(reader.credentials(root), (123, secret))
                self.assertEqual([call.args[0] for call in run.call_args_list], [
                    ["/usr/bin/security", "find-generic-password", "-a", "test-owner", "-s",
                     service, "-w", "/path/to/telegram.keychain-db"]
                    for service in ("test-id", "test-hash")
                ])
            self.assertEqual(json.loads(path.read_text()), config)
            self.assertEqual(path.stat().st_mode & 0o777, 0o600)


if __name__ == "__main__":
    unittest.main()
