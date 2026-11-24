"""Tests for exercise 6.4 - remember_remember."""
from pathlib import Path
import runpy
import tempfile
import unittest

from PIL import Image

MODULE = runpy.run_path(str(Path(__file__).parents[1] / "src" / "6.4.remember_remember.py"))


class RememberRememberTests(unittest.TestCase):
    """Decode a small image created by the test."""

    def test_decode_and_reject_bad_columns(self):
        """Read one dark pixel per column; two dark pixels raise ValueError."""
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "encoded.png"
            image = Image.new("L", (3, 256), 255)
            for column, char in enumerate("Hi!"):
                image.putpixel((column, ord(char)), 1)
            image.save(path)
            self.assertEqual(MODULE["remember_remember"](path), "Hi!")
            image.putpixel((0, 1), 0)
            image.save(path)
            with self.assertRaises(ValueError):
                MODULE["remember_remember"](path)


if __name__ == "__main__":
    unittest.main()
