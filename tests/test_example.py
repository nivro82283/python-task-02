"""Tests for the Example class."""

import unittest
from src.example import Example


class MyTestCase(unittest.TestCase):
    """Check the initial state of Example objects."""

    def test_example(self):
        """Verify that the initial value is six."""
        example = Example()
        self.assertEqual(example.x, 6)


if __name__ == "__main__":
    unittest.main()
