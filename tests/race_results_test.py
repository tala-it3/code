import unittest
from unittest.mock import patch
from main import race_results
from io import StringIO

class TestRaceResults(unittest.TestCase):
    @patch('main.read_integer_between_numbers', return_value=1)  # Mock read_integer_between_numbers
    @patch('main.reading_race_results', return_value=(['KY-43'], [1915]))  # Mock reading_race_results
    @patch('sys.stdout', new_callable=StringIO)  # Redirect stdout
    def test_race_results(self, mock_stdout, mock_reading_race_results, mock_read_integer):
        """
        Test using the first option in the race menu.
        """
        # Test data
        races_location = ["blarney", "kinsale", "newmarket", "youghal", "castletownbere"]

        ids, times, venue = race_results(races_location)

        self.assertEqual(ids, ['KY-43'])
        self.assertEqual(times, [1915])
        self.assertEqual(venue, "blarney")

        # Check mocks were called as expected
        mock_reading_race_results.assert_called_once_with("blarney")
        mock_read_integer.assert_called_once_with("Choice > ", 1, len(races_location))

        # Verify menu
        printed_output = mock_stdout.getvalue()
        self.assertIn("1: blarney", printed_output)
        self.assertIn("2: kinsale", printed_output)
        self.assertIn("5: castletownbere", printed_output)

    @patch('main.read_integer_between_numbers', return_value=3)
    @patch('main.reading_race_results', return_value=(['Runner3'], [200]))
    @patch('sys.stdout', new_callable=StringIO)
    def test_race_results_last_option(self, mock_stdout, mock_reading_race_results, mock_read_integer):
        """
        Test using the last option in the race menu.
        """
        races_location = ["Venue1", "Venue2", "Venue3"]

        ids, times, venue = race_results(races_location)

        self.assertEqual(ids, ['Runner3'])
        self.assertEqual(times, [200])
        self.assertEqual(venue, "Venue3")
        
        mock_reading_race_results.assert_called_once_with("Venue3")
        mock_read_integer.assert_called_once_with("Choice > ", 1, len(races_location))

        # Check the printed menu
        printed_output = mock_stdout.getvalue()
        self.assertIn("3: Venue3", printed_output)

if __name__ == "__main__":
    unittest.main()