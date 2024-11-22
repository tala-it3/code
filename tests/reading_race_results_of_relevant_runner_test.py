"""
Unit for function
"""

# Imports

import os
import random
import unittest

from unittest.mock import patch

import config
import utils

from main import reading_race_results_of_relevant_runner


# Tests

class AppTests(unittest.TestCase):

    # Mock tests
    location = "blarney"

    def test_generate(self):
        """
        Simple Tests
        """

        # Extract the information from the file
        file_location = os.path.join(config.INFO_FOLDER, f"{self.location.lower()}.txt")
        file_data = utils.read_text_file(file_location)
        extracted_data = utils.extract_info_text(file_data, separator=',')

        # Run the function we test
        result_runner = reading_race_results_of_relevant_runner(
            self.location,
            extracted_data[0][0]
        )
        # Compare results
        self.assertEqual(int(extracted_data[0][1]), result_runner)

        # Check function with runner not found
        result_runner = reading_race_results_of_relevant_runner(
            self.location,
            "non_existent_runner"
        )
        # Compare results
        self.assertIsNone(result_runner)

    def test_file(self):
        """
        Test file
        """
        with self.assertRaises(ValueError):
            reading_race_results_of_relevant_runner("somthing does not exist", "Test")

    def test_empty(self):
        """
        Check if we raise errors
        """

        with self.assertRaises(TypeError):
            reading_race_results_of_relevant_runner()

        with self.assertRaises(TypeError):
            reading_race_results_of_relevant_runner(["one"])

        with self.assertRaises(TypeError):
            reading_race_results_of_relevant_runner(2)

        with self.assertRaises(TypeError):
            reading_race_results_of_relevant_runner(1, 2, 4)

    def test_types(self):
        """
        Check if we raise errors
        """
        with self.assertRaises(ValueError):
            reading_race_results_of_relevant_runner([1, 2], [3, 4])

        with self.assertRaises(ValueError):
            reading_race_results_of_relevant_runner(True, False)

        with self.assertRaises(ValueError):
            reading_race_results_of_relevant_runner(("test", "other"), ("other", "test"))

        with self.assertRaises(ValueError):
            reading_race_results_of_relevant_runner(["test"], [False])
