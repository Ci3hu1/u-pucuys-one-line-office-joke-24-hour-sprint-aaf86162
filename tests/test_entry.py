"""Tests for the one-line office joke entry.

Run from the repo root: python3 -m unittest discover -s tests -v
"""

import os
import subprocess
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(REPO, "main.py")
OUT = "/output/entry.txt"


class TestEntry(unittest.TestCase):
    def run_main(self):
        result = subprocess.run(
            [sys.executable, MAIN], capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_writes_exactly_one_line_under_200_chars(self):
        self.run_main()
        with open(OUT, encoding="utf-8") as f:
            text = f.read()
        self.assertTrue(1 <= len(text) <= 200, f"char count: {len(text)}")
        lines = text.split("\n")
        # One line of text plus the single trailing newline.
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[1], "")
        self.assertTrue(lines[0].strip())

    def test_no_trailing_blank_line(self):
        self.run_main()
        with open(OUT, "rb") as f:
            raw = f.read()
        self.assertFalse(raw.endswith(b"\n\n"))
        self.assertFalse(raw.endswith(b"\r"))
        self.assertFalse(raw.endswith(b"\r\n"))

    def test_byte_identical_reruns(self):
        self.run_main()
        with open(OUT, "rb") as f:
            first = f.read()
        self.run_main()
        with open(OUT, "rb") as f:
            second = f.read()
        self.assertEqual(first, second)

    def test_output_mode_0644(self):
        self.run_main()
        self.assertEqual(oct(os.stat(OUT).st_mode & 0o777), "0o644")

    def test_stdlib_only(self):
        with open(MAIN, encoding="utf-8") as f:
            source = f.read()
        self.assertIn("import os", source)
        self.assertNotIn("import requests", source)
        self.assertNotIn("import numpy", source)


if __name__ == "__main__":
    unittest.main()
