"""Tests for exercise 5.3 - parsle_tongue."""
from pathlib import Path
import runpy
import tempfile
import unittest

MODULE = runpy.run_path(str(Path(__file__).parents[1] / "src" / "5.3.parsle_tongue.py"))


class ParsleTongueTests(unittest.TestCase):
    """Check which messages are found in a binary file."""

    def test_messages(self):
        """Skip short, uppercase and unfinished runs."""
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "messages.bin"
            path.write_bytes(b"\xffabcd!abcde!hello!\x00UPPER!world!unfinished")
            self.assertEqual(list(MODULE["parsle_tongue"](path)),
                             ["abcde!", "hello!", "world!"])


if __name__ == "__main__":
    unittest.main()
