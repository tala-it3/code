
"""
Unit testing of the `extract_info_text` utils function
"""

# Imports

import unittest
from unittest.mock import patch

from main import relevant_runner_info


# Tests

class AppTests(unittest.TestCase):

    runners = ["john", "bob"]
    ids = ["j1", "b2"]

    input_one = 1
    input_two = 2

    @patch("builtins.input", return_value=str(input_one))
    def test_input_one(self, _):
        """
        Test the first input
        """
        runner_got, id_got = relevant_runner_info(self.runners, self.ids)

        self.assertEqual(runner_got, self.runners[self.input_one - 1])
        self.assertEqual(id_got, self.ids[self.input_one - 1])

        self.assertNotEqual(runner_got, self.runners[self.input_two - 1])
        self.assertNotEqual(id_got, self.ids[self.input_two - 1])

    @patch("builtins.input", return_value=str(input_two))
    def test_input_two(self, _):
        """
        Test the second input
        """
        runner_got, id_got = relevant_runner_info(self.runners, self.ids)

        self.assertEqual(runner_got, self.runners[self.input_two - 1])
        self.assertEqual(id_got, self.ids[self.input_two - 1])

        self.assertNotEqual(runner_got, self.runners[self.input_one - 1])
        self.assertNotEqual(id_got, self.ids[self.input_one - 1])

    def test_empty(self):
        """
        Check if we raise errors
        """

        with self.assertRaises(TypeError):
            relevant_runner_info()

        with self.assertRaises(TypeError):
            relevant_runner_info(["one"])

        with self.assertRaises(ValueError):
            relevant_runner_info([], [])

        with self.assertRaises(ValueError):
            relevant_runner_info(["test"], [])

    def test_types(self):
        """
        Check if we raise errors
        """
        with self.assertRaises(ValueError):
            relevant_runner_info([1, 2], [3, 4])

        with self.assertRaises(ValueError):
            relevant_runner_info(True, False)

        with self.assertRaises(ValueError):
            relevant_runner_info(("test", "other"), ("other", "test"))

        with self.assertRaises(ValueError):
            relevant_runner_info(["test"], [False])

    def test_difference(self):
        """
        Check if we raise errors
        """
        with self.assertRaises(ValueError):
            relevant_runner_info(["test"], ["one", "two"])

        with self.assertRaises(ValueError):
            relevant_runner_info(["test", "three", "four"], ["one", "two"])
