import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import reader


class PortableMediaTests(unittest.TestCase):
    def test_image_label_cannot_turn_a_list_of_paths_into_ocr_input(self):
        with tempfile.TemporaryDirectory() as work:
            path = Path(work, "photo.jpg")
            path.write_text("other-image.png", encoding="utf-8")
            with patch.object(reader, "read_text_output") as extract:
                with self.assertRaises(ValueError):
                    reader.portable_image_text(path)
                extract.assert_not_called()

    def test_truncation_handles_partial_four_byte_character(self):
        with tempfile.TemporaryDirectory() as work:
            command = [sys.executable, "-c",
                       "import sys;sys.stdout.buffer.write(('a' + '🌐' * 9).encode())"]
            with patch.object(reader, "MAX_EXTRACTED_CHARS", 3):
                text = reader.read_text_output(command, Path(work))
                self.assertEqual(text, "a🌐🌐🌐")

    def test_missing_optional_extractors_report_the_needed_tool(self):
        with patch.object(sys, "platform", "win32"), patch.object(shutil, "which", return_value=None):
            for suffix, tool in [(".pdf", "pdftotext"), (".png", "tesseract")]:
                result = reader.extract_text(Path("example" + suffix), "messageDocument", suffix)
                self.assertEqual(result, {"status": "missing_dependencies", "tools": [tool]})

    @unittest.skipUnless(sys.platform == "darwin" or shutil.which("pdftotext"),
                         "install Poppler to exercise the platform PDF parser")
    def test_platform_extractor_reads_a_local_pdf_with_a_text_layer(self):
        stream = b"BT /F1 12 Tf 10 50 Td (Reader smoke test) Tj ET"
        objects = [b"<< /Type /Catalog /Pages 2 0 R >>",
                   b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
                   b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 300 100] "
                   b"/Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
                   b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
                   b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"\nendstream"]
        pdf = bytearray(b"%PDF-1.4\n")
        offsets = []
        for index, obj in enumerate(objects, 1):
            offsets.append(len(pdf))
            pdf.extend(b"%d 0 obj\n" % index + obj + b"\nendobj\n")
        xref = len(pdf)
        pdf.extend(b"xref\n0 6\n0000000000 65535 f \n")
        for offset in offsets:
            pdf.extend(b"%010d 00000 n \n" % offset)
        pdf.extend(b"trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % xref)
        with tempfile.TemporaryDirectory() as work:
            path = Path(work, "sample.pdf")
            path.write_bytes(pdf)
            result = reader.extract_text(path, "messageDocument", ".pdf")
            self.assertEqual(result["status"], "ok")
            self.assertEqual(result["text"].strip(), "Reader smoke test")
