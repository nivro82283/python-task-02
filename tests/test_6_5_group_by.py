"""Tests for exercise 6.5 - group_by."""
from pathlib import Path
import runpy
import unittest

MODULE = runpy.run_path(str(Path(__file__).parents[1] / "src" / "6.5.group_by.py"))


class GroupByTests(unittest.TestCase):
    """Check grouping order and duplicates."""

    def test_grouping(self):
        """Keep duplicates and the original order, also for a one-time iterator."""
        self.assertEqual(MODULE["group_by"](len, iter(["hi", "bye", "yo", "try", "hi"])),
                         {2: ["hi", "yo", "hi"], 3: ["bye", "try"]})
        self.assertEqual(MODULE["group_by"](len, []), {})


if __name__ == "__main__":
    unittest.main()
