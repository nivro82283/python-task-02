"""Tests for exercise 5.1 - no_vinnigrete."""
import datetime
from pathlib import Path
import runpy
import unittest
from unittest.mock import patch

MODULE = runpy.run_path(str(Path(__file__).parents[1] / "src" / "5.1.no_vinnigrete.py"))


class NoVinnigreteTests(unittest.TestCase):
    """Check the chosen date, invalid input and the Monday message."""

    def test_range_includes_both_ends(self):
        """Both ends of the range can be chosen, including a leap day."""
        for offset, expected in [(0, "2024-02-28"), (2, "2024-03-01")]:
            with patch.object(MODULE["random"], "randint", return_value=offset):
                result = MODULE["no_vinnigrete"]("2024-02-28", "2024-03-01")
            self.assertEqual(result, datetime.date.fromisoformat(expected))

    def test_invalid_dates(self):
        """Reject impossible dates and reversed ranges."""
        for start, end in [("2026-02-30", "2026-03-01"), ("2026-03-02", "2026-03-01")]:
            with self.assertRaises(ValueError):
                MODULE["no_vinnigrete"](start, end)

    def test_monday_message(self):
        """Print the message when the chosen date is a Monday."""
        with patch("builtins.input", side_effect=["2026-11-16"] * 2):
            with patch("builtins.print") as printer:
                MODULE["main"]()
        printer.assert_any_call("אין לי ויניגרט!")


if __name__ == "__main__":
    unittest.main()
