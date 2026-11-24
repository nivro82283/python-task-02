"""Tests for exercise 6.3 - long_cat_is_long."""
from pathlib import Path
import runpy
import unittest

MODULE = runpy.run_path(str(Path(__file__).parents[1] / "src" / "6.3.long_cat_is_long.py"))


class LongCatIsLongTests(unittest.TestCase):
    """Check word cleaning and lengths."""

    def test_word_lengths(self):
        """Lowercase words and drop punctuation and digits."""
        long_cat_is_long = MODULE["long_cat_is_long"]
        self.assertEqual(long_cat_is_long("Cat, CAT! long\ncat. 123"),
                         {"cat": 3, "long": 4})
        self.assertEqual(long_cat_is_long("... 123"), {})
        self.assertEqual(long_cat_is_long("can't"), {"cant": 4})


if __name__ == "__main__":
    unittest.main()
