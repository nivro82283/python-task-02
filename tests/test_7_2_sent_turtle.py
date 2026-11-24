"""Tests for exercise 7.2 - sent_turtle (PostOffice)."""
from pathlib import Path
import runpy
import unittest

MODULE = runpy.run_path(str(Path(__file__).parents[1] / "src" / "7.2.sent_turtle.py"))


class PostOfficeTests(unittest.TestCase):
    """Check reading, searching and errors."""

    def test_read_inbox(self):
        """Urgent mail comes first and read mail is not returned again."""
        office = MODULE["PostOffice"](["a", "b"])
        first = office.send_message("a", "b", "normal")
        urgent = office.send_message("a", "b", "urgent", True)
        self.assertEqual(office.read_inbox("b", 0), [])
        self.assertEqual([msg["id"] for msg in office.read_inbox("b", 1)], [urgent])
        self.assertEqual([msg["id"] for msg in office.read_inbox("b", 50)], [first])
        self.assertEqual(office.read_inbox("b"), [])

    def test_search_inbox(self):
        """Search title and body, including read mail, without marking it read."""
        office = MODULE["PostOffice"](["a", "b"])
        office.send_message("a", "b", "body", title="needle")
        office.send_message("a", "b", "needle in body")
        self.assertEqual(len(office.search_inbox("b", "needle")), 2)
        self.assertEqual(len(office.read_inbox("b")), 2)
        self.assertEqual(len(office.search_inbox("b", "needle")), 2)
        self.assertEqual(office.search_inbox("b", "missing"), [])

    def test_errors(self):
        """Reject unknown recipients and bad counts."""
        office = MODULE["PostOffice"](["a"])
        with self.assertRaises(KeyError):
            office.send_message("a", "missing", "hello")
        with self.assertRaises(ValueError):
            office.read_inbox("a", -1)
        with self.assertRaises(TypeError):
            office.read_inbox("a", 1.5)


if __name__ == "__main__":
    unittest.main()
