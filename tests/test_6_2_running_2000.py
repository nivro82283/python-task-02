"""Tests for exercise 6.2 - running_2000."""
from pathlib import Path
import runpy
import unittest
from unittest.mock import Mock, patch

MODULE = runpy.run_path(str(Path(__file__).parents[1] / "src" / "6.2.running_2000.py"))


class Running2000Tests(unittest.TestCase):
    """Check the arguments passed on and the measured time."""

    def test_arguments_and_elapsed_time(self):
        """Call the function once with all arguments and return the elapsed time."""
        function = Mock(return_value=12)
        with patch.object(MODULE["time"], "perf_counter", side_effect=[10.0, 10.25]):
            elapsed = MODULE["running_2000"](function, 3, name="Bug")
        self.assertEqual(elapsed, 0.25)
        function.assert_called_once_with(3, name="Bug")

    def test_errors_are_not_hidden(self):
        """An error inside the function reaches the caller."""
        with self.assertRaises(ValueError):
            MODULE["running_2000"](Mock(side_effect=ValueError("failure")))


if __name__ == "__main__":
    unittest.main()
