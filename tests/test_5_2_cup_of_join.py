"""Tests for exercise 5.2 - cup_of_join."""
from pathlib import Path
import runpy
import unittest

MODULE = runpy.run_path(str(Path(__file__).parents[1] / "src" / "5.2.cup_of_join.py"))


class CupOfJoinTests(unittest.TestCase):
    """Check the notebook examples and edge cases."""

    def test_notebook_examples(self):
        """Use a custom separator, the default one, one list and no lists."""
        cup_of_join = MODULE["cup_of_join"]
        self.assertEqual(cup_of_join([1, 2], [8], [9, 5, 6], sep="@"),
                         [1, 2, "@", 8, "@", 9, 5, 6])
        self.assertEqual(cup_of_join([1], [2]), [1, "-", 2])
        self.assertEqual(cup_of_join([1]), [1])
        self.assertIsNone(cup_of_join())

    def test_inputs_are_not_changed(self):
        """Keep separators around empty lists and leave the inputs unchanged."""
        values = [1]
        self.assertEqual(MODULE["cup_of_join"]([], values, [], sep="x"), ["x", 1, "x"])
        self.assertEqual(values, [1])


if __name__ == "__main__":
    unittest.main()
