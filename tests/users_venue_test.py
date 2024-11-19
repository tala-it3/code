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

from main import users_venue

# Range of fake times
LOWER_TIME = 0
UPPER_TIME = 5000


# Tests

class AppTests(unittest.TestCase):

    # Mock data
    runners = ["one", "two", "three"]
    races_location = ["somewhere", "else"]
    races_means = ["32.5", "12"]
    location = "testing"
    location_path = os.path.join(config.INFO_FOLDER, f"{location.lower()}.txt")
    # Generate fake times
    times = [random.randint(LOWER_TIME, UPPER_TIME) for _ in runners]
    # Calculate fake mean
    mean = round((sum(times) / len(times) / config.SECONDS_IN_MINUTES) * 2) / 2

    # Mock data string
    mock_data_string = [location] + [
        str(each_time) for each_time in times
    ]

    @patch("builtins.input", side_effect=mock_data_string)
    def test_generate(self, _):
        """
        Simple Tests
        """

        # Remove the test file if present
        if os.path.isfile(self.location_path):
            os.remove(self.location_path)

        # Run the function
        users_venue(self.races_location, self.races_means, self.runners)

        # Read the newly created file and compare
        file_data = utils.extract_info_text(
            utils.read_text_file(self.location_path)
        )

        # Compare the data
        for index, item in enumerate(file_data):
            self.assertEqual(item[0], self.runners[index])
            self.assertEqual(item[1], str(self.times[index]))

        # Check if the lists have updated
        self.assertTrue(self.location in self.races_location)

        # Check if the time is also added
        self.assertTrue(str(self.mean) in self.races_means)

        # Remove the test file
        if os.path.isfile(self.location_path):
            os.remove(self.location_path)

    @patch("builtins.input", return_value=races_location[0])
    def test_recursion(self, _):
        """
        Input Recursion
        """

        with self.assertRaises(RecursionError):
            users_venue(self.races_location, self.races_means, self.runners)

    def test_empty(self):
        """
        Check if we raise errors
        """

        with self.assertRaises(TypeError):
            users_venue()

        with self.assertRaises(TypeError):
            users_venue(["one"])

        with self.assertRaises(ValueError):
            users_venue([], [],[])

        with self.assertRaises(ValueError):
            users_venue(["test"], [],[])

    def test_types(self):
        """
        Check if we raise errors
        """
        with self.assertRaises(ValueError):
            users_venue([1, 2], [3, 4], [5, 6])

        with self.assertRaises(ValueError):
            users_venue(True, False, None)

        with self.assertRaises(ValueError):
            users_venue(("test", "other"), ("other", "test"), ("a", "b"))

        with self.assertRaises(ValueError):
            users_venue(["test"], [False], [12])
