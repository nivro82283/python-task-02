"""Tests for exercise 5.2 - piece_of_cake."""
from pathlib import Path
import runpy
import unittest

MODULE = runpy.run_path(str(Path(__file__).parents[1] / "src" / "5.2.piece_of_cake.py"))


class PieceOfCakeTests(unittest.TestCase):
    """Check the notebook examples."""

    def test_notebook_examples(self):
        """Weight prices per 100 grams and skip optional ingredients."""
        piece_of_cake = MODULE["piece_of_cake"]
        prices = {"chocolate": 18, "milk": 8}
        self.assertEqual(piece_of_cake(prices, chocolate=200, milk=100), 44)
        self.assertEqual(piece_of_cake(prices, optionals=["milk"], chocolate=300), 54)
        self.assertEqual(piece_of_cake({}), 0)


if __name__ == "__main__":
    unittest.main()
