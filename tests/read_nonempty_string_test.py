
"""
Unit testing of the `extract_info_text` utils function
"""

# Imports

import unittest
from unittest.mock import patch

from main import read_nonempty_string


# Tests

class AppTests(unittest.TestCase):

    input_string_right = "test"
    input_string_wrong = "test wrong"

    @patch("builtins.input", return_value=input_string_right)
    def test_pass(self, _):
        """
        Simple Tests
        """
        self.assertEqual(read_nonempty_string("Test "), self.input_string_right)

    @patch("builtins.input", return_value=input_string_wrong)
    def test_fail(self, _):
        """
        Fail on infinite loop
        """
        with self.assertRaises(RecursionError):
            read_nonempty_string("Test ")

    def test_errors(self):
        """
        Check if we raise errors
        """
        with self.assertRaises(TypeError):
            read_nonempty_string(12)

        with self.assertRaises(TypeError):
            read_nonempty_string(False)

        with self.assertRaises(TypeError):
            read_nonempty_string([])

        with self.assertRaises(TypeError):
            read_nonempty_string({})
