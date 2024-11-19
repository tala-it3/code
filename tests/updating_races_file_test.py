"""
Unit testing of the `updating_races_file` utils function
"""

# Imports

import os
import random
import unittest

from unittest.mock import patch

import config
import utils

from main import updating_races_file

# Path to the races file
RACES_OG = os.path.join(config.ASSETS_FOLDER, "races.txt")
RACES_BACKUP = os.path.join(config.ASSETS_FOLDER, "races-backup.txt")


# Tests

class AppTests(unittest.TestCase):

    # Mock data
    races_location = ["somewhere", "else"]
    races_means = ["32.5", "12"]

    def test_generate(self):
        """
        Simple Tests
        """

        # Store the original file
        os.rename(RACES_OG, RACES_BACKUP)

        # Run the function
        updating_races_file(self.races_location, self.races_means)

        # Read the newly created file and compare
        file_data = utils.extract_info_text(
            utils.read_text_file(RACES_OG)
        )

        # Compare the data
        for index, item in enumerate(file_data):
            self.assertEqual(self.races_location[index].capitalize(), item[0])
            self.assertEqual(self.races_means[index], item[1])

        # Restore the file
        os.rename(RACES_BACKUP, RACES_OG)

    def test_empty(self):
        """
        Check if we raise errors
        """

        with self.assertRaises(TypeError):
            updating_races_file()

        with self.assertRaises(TypeError):
            updating_races_file(["one"])

        with self.assertRaises(ValueError):
            updating_races_file([], [])

        with self.assertRaises(ValueError):
            updating_races_file(["test"], [])

    def test_types(self):
        """
        Check if we raise errors
        """
        with self.assertRaises(ValueError):
            updating_races_file([1, 2], [3, 4])

        with self.assertRaises(ValueError):
            updating_races_file(True, False)

        with self.assertRaises(ValueError):
            updating_races_file(("test", "other"), ("other", "test"))

        with self.assertRaises(ValueError):
            updating_races_file(["test"], [False])
