"""Tests for exercise 5.1 - thats_the_way."""
from pathlib import Path
import runpy
import tempfile
import unittest

MODULE = runpy.run_path(str(Path(__file__).parents[1] / "src" / "5.1.thats_the_way.py"))


class ThatsTheWayTests(unittest.TestCase):
    """Check which file names are returned."""

    def test_only_files_starting_with_deep(self):
        """Return matching files only, case-sensitively and without folders."""
        with tempfile.TemporaryDirectory() as folder:
            for name in ["deep.txt", "deeper.svg", "Deep.txt", "other.txt"]:
                (Path(folder) / name).touch()
            (Path(folder) / "deep_folder").mkdir()
            self.assertEqual(set(MODULE["thats_the_way"](folder)),
                             {"deep.txt", "deeper.svg"})


if __name__ == "__main__":
    unittest.main()
