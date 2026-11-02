"""Regression checks for image contributions and existing documentation rules."""

import base64
import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    "check_docs", Path(__file__).resolve().parents[1] / "scripts/check_docs.py"
)
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)
GIF = base64.b64decode("R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==")
PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aOuEAAAAASUVORK5CYII="
)


class DocumentationChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        root_patch = patch.object(CHECK, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        for topic in CHECK.TOPICS:
            self.write(f"{topic}/README.md", "# Index\n")

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            path.write_bytes(content)
        else:
            path.write_text(content, encoding="utf-8")

    def check(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = CHECK.main()
        return result, output.getvalue()

    def test_image_contribution_with_nested_character_folder(self):
        self.write("memes/images/灭霸/reaction.GIF", GIF)
        self.write("memes/README.md", "# Index\n![reaction](images/灭霸/reaction.GIF)\n")
        result, output = self.check()
        self.assertEqual(result, 0, output)
        self.assertIn("1 images", output)

    def test_supported_image_headers(self):
        # JPEG and WebP fixtures exercise header recognition, not full decoding.
        fixtures = {
            "a.png": PNG, "b.gif": GIF,
            "c.jpg": b"\xff\xd8\xff\xe0", "d.jpeg": b"\xff\xd8\xff\xe0",
            "e.webp": b"RIFF\x04\x00\x00\x00WEBP",
        }
        for name, content in fixtures.items():
            self.write(f"assets/{name}", content)
        result, output = self.check()
        self.assertEqual(result, 0, output)

    def test_wrong_image_extension_fails(self):
        self.write("assets/fake.jpg", GIF)
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("image header does not match", output)

    def test_missing_image_link_still_fails(self):
        self.write("memes/README.md", "![missing](images/missing.png)\n")
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("missing link target", output)

    def test_documentation_folder_still_needs_index(self):
        self.write("memes/images/note.md", "# Source notes\n")
        self.write("memes/images/sample.gif", GIF)
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("memes/images: missing README index", output)

    def test_unknown_binary_still_fails(self):
        self.write("assets/unknown.bin", b"\xff\xfe\x00")
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("expected a UTF-8 text file", output)

    def test_private_file_still_fails(self):
        self.write(".env", "EXAMPLE=value\n")
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("local data does not belong", output)

    def test_image_extension_does_not_allow_private_filename(self):
        self.write(".env.png", PNG)
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("local data does not belong", output)

    def test_credentials_in_text_still_fail(self):
        self.write("notes.md", "sk-" + "a" * 30)
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("possible credential", output)

    def test_links_outside_repository_still_fail(self):
        self.write("memes/README.md", "[outside](../../outside.md)\n")
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("local link leaves the repository", output)


if __name__ == "__main__":
    unittest.main()
