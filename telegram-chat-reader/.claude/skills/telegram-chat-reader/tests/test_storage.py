import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import reader


class StorageTests(unittest.TestCase):
    def test_new_private_directory_and_atomic_json_replacement(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = reader.private_directory(Path(temporary) / "session")
            path = directory / "account.json"
            self.assertIsNone(reader.read_private_json(path))
            for value in ({"account": "first"}, {"account": "second"}):
                reader.write_private_json(path, value)
                self.assertEqual(reader.read_private_json(path), value)
            self.assertEqual(list(directory.iterdir()), [path])

    def test_another_process_cannot_use_session_until_lock_is_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = reader.private_directory(Path(temporary) / "session")
            cmd = [sys.executable, "-c", """
import reader, sys
from pathlib import Path
try:
    with reader.session_lock(Path(sys.argv[1])):
        pass
except reader.ReaderError:
    sys.exit(2)
""", str(root)]
            with reader.session_lock(root):
                self.assertEqual(subprocess.run(cmd, cwd=SCRIPTS).returncode, 2)
            self.assertEqual(subprocess.run(cmd, cwd=SCRIPTS).returncode, 0)

    @unittest.skipUnless(os.name == "nt", "Windows NTFS DACL")
    def test_existing_directory_grant_to_everyone_is_rejected_without_rewriting_it(self):
        import win32file
        import win32security
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "public"
            user = reader.windows_user_sid()
            attributes = win32security.SECURITY_ATTRIBUTES()
            sddl = f"O:{user}D:P(A;OICI;FA;;;{user})(A;OICI;FR;;;WD)"
            attributes.SECURITY_DESCRIPTOR = win32security.ConvertStringSecurityDescriptorToSecurityDescriptor(sddl, 1)
            win32file.CreateDirectory(str(path), attributes)
            for _ in range(2):
                with self.assertRaises(reader.ReaderError):
                    reader.private_directory(path)

    @unittest.skipUnless(sys.platform.startswith("linux"), "XDG state directory selection")
    def test_xdg_accepts_absolute_paths_and_ignores_relative_values(self):
        with patch.dict(os.environ, {"XDG_DATA_HOME": "/isolated/data"}):
            self.assertEqual(reader.state_directory(), Path("/isolated/data/telegram-chat-reader"))
        with patch.dict(os.environ, {"XDG_DATA_HOME": "relative"}):
            self.assertEqual(reader.state_directory(), Path.home() / ".local/share/telegram-chat-reader")
