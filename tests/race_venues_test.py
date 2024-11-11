import unittest
from main import race_venues
from unittest.mock import mock_open, patch

class TestRaceVenues(unittest.TestCase):
    """
    Unit test class for testing the race_venues function.
    """

    def test_race_venues(self):
        """
        Test case for a normal file with valid race venue data.
        """
        # Mock the content of the 'races.txt' file
        mock_file_content = "Kinsale, 30\nBlarney, 32\nNewmarket, 29\nYoughal, 29.5\nCastletownbere, 32.5\n"
        
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            result = race_venues()
        
        # Expected result after reading the file
        expected = ["Kinsale", "Blarney", "Newmarket", "Youghal", "Castletownbere"]
        
        # Assert that the result matches the expected list of venue names
        self.assertEqual(result, expected)

    def test_empty_file(self):
        """
        Test case for an empty file.
        """
        # Test with an empty file
        mock_file_content = ""
        
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            result = race_venues()
        
        # The expected result for an empty file is an empty list
        self.assertEqual(result, [])

    def test_file_with_extra_spaces(self):
        """
        Test case for a file with extra spaces around the venue names.
        """
        # Test file with extra spaces around the venue names
        mock_file_content = " Kinsale , 30 \n Blarney , 32 \nNewmarket, 29\n"
        
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            result = race_venues()
        
        # The expected result should have stripped spaces from the names
        expected = ["Kinsale", "Blarney", "Newmarket"]
        self.assertEqual(result, expected)

    def test_file_with_newline_at_end(self):
        """
        Test case for a file with a trailing newline at the end.
        """
        # Test file with a trailing newline
        mock_file_content = "Kinsale, 30\nBlarney, 32\nNewmarket, 29\n"
        
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            result = race_venues()
        
        # The expected result should be the same as before, just without trailing newlines
        expected = ["Kinsale", "Blarney", "Newmarket"]
        self.assertEqual(result, expected)

    def test_file_with_blank_lines(self):
        """
        Test case for a file with blank lines in between.
        """
        # Test file with blank lines in between
        mock_file_content = "Kinsale, 30\n\nBlarney, 32\n\nNewmarket, 29\n"
        
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            result = race_venues()
        
        # The expected result should not include any empty venue names (ignore blank lines)
        expected = ["Kinsale", "Blarney", "Newmarket"]
        self.assertEqual(result, expected)

    def test_file_with_extra_newlines_and_spaces(self):
        """
        Test case for a file with extra newlines and spaces at the beginning and end.
        """
        # Test file with extra spaces and newlines at the beginning and end
        mock_file_content = "\n\n  Kinsale, 30  \n\nBlarney, 32\n\nNewmarket, 29\n\n"
        
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            result = race_venues()

        # The expected result should be stripped and without extra blank lines or spaces
        expected = ["Kinsale", "Blarney", "Newmarket"]
        self.assertEqual(result, expected)