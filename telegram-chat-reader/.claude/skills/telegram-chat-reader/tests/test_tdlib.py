import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import reader


class LibraryTests(unittest.TestCase):
    def test_explicit_library_path_takes_precedence_over_installed_wheel(self):
        missing = str(Path(__file__).resolve().with_name("absent-library"))
        with patch.dict(os.environ, {"TDJSON_LIBRARY": missing}):
            with self.assertRaises(reader.ReaderError):
                reader.TDLib()

    @unittest.skipUnless(os.environ.get("TELEGRAM_READER_TEST_NATIVE_TDLIB") == "1",
                         "Set TELEGRAM_READER_TEST_NATIVE_TDLIB=1 to exercise native TDLib")
    def test_native_library_handles_offline_client_lifecycle(self):
        with reader.TDLib() as td:
            td.client_id = td.lib.td_create_client_id()
            state = td.request("getAuthorizationState")
            self.assertEqual(state["@type"], "authorizationStateWaitTdlibParameters")
