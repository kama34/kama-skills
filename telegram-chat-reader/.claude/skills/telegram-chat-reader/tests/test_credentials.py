import os
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch
from uuid import uuid4

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import reader


class NativeCredentialTests(unittest.TestCase):
    def test_setup_resumes_in_both_stores_and_only_saves_a_reference(self):
        for platform, name in (("win32", "Windows Credential Manager"), ("linux", "Secret Service")):
            with self.subTest(platform=platform):
                store = Mock()
                saved = {"telegram-chat-reader.api_id": "123"}
                store.get_password.side_effect = lambda service, account: saved.get(service)
                def save(service, account, value):
                    saved[service] = value
                store.set_password.side_effect = save
                reference = {"credential_store": name}
                root = Path("test-state")
                with patch.object(reader.sys, "platform", platform), \
                        patch.object(reader, "native_credential_store", return_value=store), \
                        patch.object(reader, "hidden_input", return_value="b" * 32) as prompt, \
                        patch.object(reader, "read_private_json", side_effect=[None, reference, reference]), \
                        patch.object(reader, "write_private_json") as write:
                    reader.configure_credentials(root)
                    reader.configure_credentials(root)
                    self.assertEqual(reader.credentials(root), (123, "b" * 32))
                prompt.assert_called_once()
                store.set_password.assert_called_once_with("telegram-chat-reader.api_hash",
                                                           "telegram-chat-reader", "b" * 32)
                write.assert_called_once_with(root / "credentials.json", reference)

    def test_read_cannot_prompt_or_write_when_locked(self):
        store = Mock()
        store.get_password.side_effect = RuntimeError("private backend diagnostic")
        with patch.object(reader.sys, "platform", "linux"), \
                patch.object(reader, "native_credential_store", return_value=store), \
                patch.object(reader, "hidden_input") as prompt, \
                patch.object(reader, "write_private_json") as write:
            with self.assertRaises(reader.ReaderError) as raised:
                reader.system_store_values(setup=False)
        self.assertNotIn("private backend diagnostic", str(raised.exception))
        prompt.assert_not_called()
        store.set_password.assert_not_called()
        write.assert_not_called()

    def test_bad_input_is_not_saved(self):
        store = Mock()
        store.get_password.return_value = None
        with patch.object(reader, "native_credential_store", return_value=store), \
                patch.object(reader, "hidden_input", return_value="wrong"):
            with self.assertRaisesRegex(reader.ReaderError, "Invalid api_id"):
                reader.system_store_values(setup=True)
        store.set_password.assert_not_called()

    @unittest.skipUnless(os.environ.get("TELEGRAM_READER_TEST_NATIVE_STORE") == "1"
                         and sys.platform in ("win32", "linux"),
                         "opt in on an isolated Windows or Linux host with an unlocked store")
    def test_native_credential_store_round_trip(self):
        store = reader.native_credential_store()
        service = f"telegram-chat-reader.test.{uuid4()}"
        value = uuid4().hex
        self.assertIsNone(store.get_password(service, "test"))
        store.set_password(service, "test", value)
        try:
            self.assertEqual(store.get_password(service, "test"), value)
        finally:
            store.delete_password(service, "test")
        self.assertIsNone(store.get_password(service, "test"))
