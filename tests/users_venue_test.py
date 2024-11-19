"""
Unit testing of the `read_text_file` utils function
"""

# Imports

import os
import random
import unittest

from unittest.mock import patch

import config
import utils

from main import (users_venue,
                  race_venues,
                  runners_data)

# Range of fake times
LOWER_TIME = 0
UPPER_TIME = 5000


# Tests

class AppTests(unittest.TestCase):

    # Mock data
    runners = ["one", "two", "three"]
    races_location = ["somewhere", "else"]
    location = "testing"
    location_path = os.path.join(config.INFO_FOLDER, f"{location.lower()}.txt")
    # Generate fake times
    times = [random.randint(LOWER_TIME, UPPER_TIME) for _ in runners]

    # Mock data string
    mock_data_string = [location] + [
        str(each_time) for each_time in times
    ]

    @patch("builtins.input", side_effect=mock_data_string)
    def test_generate(self, _):
        """
        Simple Tests
        """

        # Run the function
        users_venue(self.races_location, self.runners)

        # Read the newly created file and compare
        file_data = utils.extract_info_text(
            utils.read_text_file(self.location_path)
        )

        # Compare the data
        for index, item in enumerate(file_data):
            self.assertEqual(item[0], self.runners[index])
            self.assertEqual(item[1], str(self.times[index]))

        # Remove the test file
        os.remove(self.location_path)

    @patch("builtins.input", return_value=races_location[0])
    def test_recursion(self, _):
        """
        Input Recursion
        """

        with self.assertRaises(RecursionError):
            users_venue(self.races_location, self.runners)

    def test_empty(self):
        """
        Check if we raise errors
        """

        with self.assertRaises(TypeError):
            users_venue()

        with self.assertRaises(TypeError):
            users_venue(["one"])

        with self.assertRaises(ValueError):
            users_venue([], [])

        with self.assertRaises(ValueError):
            users_venue(["test"], [])

    def test_types(self):
        """
        Check if we raise errors
        """
        with self.assertRaises(ValueError):
            users_venue([1, 2], [3, 4])

        with self.assertRaises(ValueError):
            users_venue(True, False)

        with self.assertRaises(ValueError):
            users_venue(("test", "other"), ("other", "test"))

        with self.assertRaises(ValueError):
            users_venue(["test"], [False])
