"""Tests for student management functions."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from students import list_students


class TestListStudents(unittest.TestCase):
    def test_returns_non_empty_names(self):
        self.assertEqual(list_students(["Asha", "Ravi"]), ["Asha", "Ravi"])

    def test_trims_whitespace_and_ignores_empty_names(self):
        self.assertEqual(list_students([" Asha ", "", "  ", "Meera"]), ["Asha", "Meera"])


if __name__ == "__main__":
    unittest.main()
