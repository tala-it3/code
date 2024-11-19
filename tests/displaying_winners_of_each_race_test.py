
"""
Unit testing of the `extract_info_text` utils function
"""

# Imports

import io
import re

import unittest
from unittest.mock import patch

from main import (displaying_winners_of_each_race,
                  reading_race_results,
                  race_venues,
                  winner_of_race)


# Tests

class AppTests(unittest.TestCase):

    # Get some needed data
    venues, _ = race_venues()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, mock_output):
        """
        Test with given inputs
        """

        # Run it
        displaying_winners_of_each_race(self.venues)

        # Get output
        output_string = mock_output.getvalue()

        # Clear it
        clean_lines = [line for line in output_string.splitlines() if line]
        # Remove headers
        no_headers = clean_lines[2:]
        list_venue_winner = [re.split(" {2,}", line) for line in no_headers]

        # Iterate list so that we can assert
        for index in range(len(self.venues)):
            self.assertEqual(
                self.venues[index], list_venue_winner[index][0]
            )
            self.assertEqual(
                winner_of_race(*reading_race_results(self.venues[index])), list_venue_winner[index][1]
            )

    def test_empty(self):
        """
        Check if we raise errors
        """

        with self.assertRaises(TypeError):
            displaying_winners_of_each_race()

        with self.assertRaises(ValueError):
            displaying_winners_of_each_race([])

    def test_types(self):
        """
        Check if we raise errors
        """
        with self.assertRaises(ValueError):
            displaying_winners_of_each_race([1, 2])

        with self.assertRaises(ValueError):
            displaying_winners_of_each_race(True)

        with self.assertRaises(ValueError):
            displaying_winners_of_each_race(("test", "other"))

        with self.assertRaises(ValueError):
            displaying_winners_of_each_race([False])
