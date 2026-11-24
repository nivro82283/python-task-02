"""Tests for exercise 5.4 - interleaves and generator_interleaves."""
from pathlib import Path
import runpy
import unittest

MODULE = runpy.run_path(str(Path(__file__).parents[1] / "src" / "5.4.interleaves.py"))


class InterleavesTests(unittest.TestCase):
    """Check the list version and the generator version."""

    def test_notebook_example(self):
        """Both versions give the notebook result."""
        expected = ["a", 1, "!", "b", 2, "@", "c", 3, "#"]
        self.assertEqual(MODULE["interleaves"]("abc", [1, 2, 3], ("!", "@", "#")), expected)
        self.assertEqual(list(MODULE["generator_interleaves"](
            iter("abc"), iter([1, 2, 3]), iter(("!", "@", "#")))), expected)

    def test_unequal_and_empty_inputs(self):
        """Stop at the shortest input."""
        interleaves = MODULE["interleaves"]
        self.assertEqual(interleaves("ab", [1]), ["a", 1])
        self.assertEqual(interleaves(), [])
        self.assertEqual(interleaves([], [1]), [])

    def test_generator_is_lazy(self):
        """No value is read before iteration starts."""
        values = iter([1, 2])
        result = MODULE["generator_interleaves"](values)
        self.assertEqual(next(values), 1)
        self.assertEqual(list(result), [2])


if __name__ == "__main__":
    unittest.main()
