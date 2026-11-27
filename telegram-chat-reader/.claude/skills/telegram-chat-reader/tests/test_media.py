import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import reader


def message(number, kind, **content):
    return {
        "@type": "message", "id": number, "chat_id": 11, "date": 100 + number,
        "can_be_saved": True, "sender_id": {"@type": "messageSenderUser", "user_id": 11},
        "content": {"@type": kind, **content},
    }


def photo(number=2):
    return message(number, "messagePhoto", photo={"sizes": [
        {"width": 10, "height": 10, "photo": {"@type": "file", "id": 1}},
        {"width": 40, "height": 40, "photo": {"@type": "file", "id": 2,
         "local": {"path": "/private/tdlib"}, "remote": {"id": "private"}}},
    ]})


class MediaTests(unittest.TestCase):
    def scope(self, **kwargs):
        scope = Mock(folder=None, folder_id=None)
        scope.resolve.return_value = {"id": 11, "title": "test", "type": {"@type": "chatTypePrivate"}}
        scope.td.state = reader.State()
        scope.read.side_effect = kwargs.get("responses", ())
        return scope

    def test_all_types_retain_captionless_and_unknown_messages_but_skip_protected(self):
        messages = [
            message(5, "messageFuture", option={"text": "test"}),
            dict(photo(4), can_be_saved=False),
            message(3, "messagePinMessage", message_id=1),
            photo(),
            message(1, "messageText", text={"text": "hello"}),
        ]
        scope = self.scope(responses=[{"@type": "messages", "messages": messages},
                                       {"@type": "messages", "messages": []}])
        result = reader.history(scope, "11", 100, None, 10, all_types=True)
        self.assertEqual([m["id"] for m in messages if m["id"] != 4][::-1],
                         [m["message_id"] for m in result["messages"]])
        self.assertNotIn("/private/tdlib", str(result))
        self.assertNotIn("'remote'", str(result))
        self.assertEqual(result["omitted_protected"], 1)
        self.assertFalse(result["complete"])

    def test_legacy_history_ignores_media_without_caption(self):
        scope = self.scope(responses=[{"@type": "messages", "messages": [
            photo(), message(1, "messageText", text={"text": "hello"}),
        ]}, {"@type": "messages", "messages": []}])
        result = reader.history(scope, "11", 100, None, 10)
        self.assertEqual([m["text"] for m in result["messages"]], ["hello"])
        self.assertNotIn("content", result["messages"][0])

    def test_protected_message_is_refused_before_download(self):
        scope = self.scope(responses=[dict(photo(), can_be_saved=False)])
        with self.assertRaises(reader.ReaderError):
            reader.fetch_media(scope, 11, 2)
        scope.download.assert_not_called()

    def test_selects_largest_photo_and_refuses_download_outside_cache(self):
        scope = self.scope(responses=[photo(), photo()])
        with tempfile.TemporaryDirectory() as work:
            source = Path(work, "source")
            source.write_bytes(b"image")
            with tempfile.TemporaryDirectory() as cache:
                scope.download.return_value = {"@type": "file", "id": 2, "local": {
                    "is_downloading_completed": True, "path": str(source),
                }}
                with self.assertRaises(reader.ReaderError):
                    reader.media_path(scope, 11, 2, Path(cache), reader.media_file(photo())[0])
        self.assertEqual(scope.download.call_args.args[:2], (11, 2))

    def test_cached_voice_transcript_avoids_media_download(self):
        voice = message(2, "messageVoiceNote", voice_note={
            "speech_recognition_result": {"@type": "speechRecognitionResultText", "text": "готовый текст"},
        })
        scope = self.scope(responses=[voice])
        result = reader.transcribe(scope, 11, 2, None, SimpleNamespace(language="ru", model=None))
        self.assertEqual(result["text"], "готовый текст")
        self.assertEqual(result["source"], "telegram")
        scope.download.assert_not_called()

    def test_video_note_falls_back_to_local_asr(self):
        note = message(2, "messageVideoNote", video_note={"video": {"@type": "file", "id": 9}})
        scope = self.scope(responses=[note, note])
        with patch.object(reader, "media_path", return_value=Path("/tmp/clip")), \
                patch.object(reader, "local_transcript", return_value="звук из кружка"):
            result = reader.transcribe(scope, 11, 2, Path("/tmp"), SimpleNamespace(language="ru", model=None))
        self.assertEqual(result["text"], "звук из кружка")
        self.assertEqual(result["source"], "local_whisper")
