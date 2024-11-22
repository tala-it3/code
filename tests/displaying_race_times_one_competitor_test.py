"""
Unit testing for function
"""

# Imports

import os
import io
import random

import unittest
from unittest.mock import patch

import config
import utils

from main import (displaying_race_times_one_competitor,
                  convert_time_to_minutes_and_seconds)

# Range of fake times
LOWER_TIME = 0
UPPER_TIME = 5000


# Tests

class AppTests(unittest.TestCase):

    # Generate false information
    locations = ["somewhere", "else"]
    runner_id = "TS-01"
    runner_name = "Testing"
    times = [random.randint(LOWER_TIME, UPPER_TIME) for _ in locations]

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, mock_output):
        """
        Test with given inputs
        """

        # Generate the runner files to test
        for location, time_run in zip(self.locations, self.times):
            with utils.open_text_file_write(
                    os.path.join(config.INFO_FOLDER, f"{location.lower()}.txt"), append=False
            ) as location_file:
                print(self.runner_id, time_run, sep=',', file=location_file)

        # Run the function it
        displaying_race_times_one_competitor(self.locations, self.runner_name, self.runner_id)

        # Extract its output
        output_string = mock_output.getvalue()

        # Extract the usable lines
        clean_lines = [line for line in output_string.splitlines() if line]
        # Remove headers
        no_headers = clean_lines[2:]

        # Check if the output length is right
        self.assertEqual(len(self.locations), len(no_headers))

        # Iterate each information line and extract data
        for location_original, time_original, line in zip(self.locations, self.times, no_headers):

            # Extract information
            location, time_position = [each.strip() for each in line.split("-")]

            # Calculate the timings
            minutes, seconds = convert_time_to_minutes_and_seconds(time_original)

            # Extract further information from text
            split_line = time_position.split()
            clear_information = list(filter(None, [
                "".join([character for character in item if character.isdigit()])
                for item in split_line
            ]))

            # Compare everything
            self.assertEqual(minutes, int(clear_information[0]))
            self.assertEqual(seconds, int(clear_information[1]))
            self.assertEqual(1, int(clear_information[2]))
            self.assertEqual(1, int(clear_information[3]))

            # Make sure it works
            self.assertNotEqual(seconds, int(clear_information[0]))
            self.assertNotEqual(minutes, int(clear_information[1]))
            self.assertNotEqual(2, int(clear_information[2]))
            self.assertNotEqual(2, int(clear_information[3]))
            self.assertNotEqual(0, int(clear_information[2]))
            self.assertNotEqual(0, int(clear_information[3]))

        # Delete the test files
        for location in self.locations:
            os.remove(os.path.join(config.INFO_FOLDER, f"{location.lower()}.txt"))

    def test_empty(self):
        """
        Check if we raise errors
        """

        with self.assertRaises(TypeError):
            displaying_race_times_one_competitor()

        with self.assertRaises(TypeError):
            displaying_race_times_one_competitor([])

        with self.assertRaises(TypeError):
            displaying_race_times_one_competitor(1, 2)

        with self.assertRaises(TypeError):
            displaying_race_times_one_competitor([], ())

        with self.assertRaises(TypeError):
            displaying_race_times_one_competitor(False, True)

    def test_wrong(self):
        """
        Check if we raise errors with wrong items
        """
        with self.assertRaises(ValueError):
            displaying_race_times_one_competitor([], "test", "test")

        with self.assertRaises(ValueError):
            displaying_race_times_one_competitor([1, 2, 3], "test", "test")

        with self.assertRaises(ValueError):
            displaying_race_times_one_competitor([True, False], "test", "test")

    def test_types(self):
        """
        Check if we raise errors
        """
        with self.assertRaises(ValueError):
            displaying_race_times_one_competitor(1, 2, 3)

        with self.assertRaises(ValueError):
            displaying_race_times_one_competitor(True, False, True)

        with self.assertRaises(ValueError):
            displaying_race_times_one_competitor(("test", "other"), 123, 432)

        with self.assertRaises(ValueError):
            displaying_race_times_one_competitor([False, True], True, False)
