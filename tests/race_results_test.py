import unittest
from unittest.mock import patch


# Assume `read_integer_between_numbers` and `reading_race_results` are imported from your module.

class TestRaceResults(unittest.TestCase):
    @patch('your_module.reading_race_results')
    @patch('your_module.read_integer_between_numbers')
    def test_race_results(self, mock_read_integer, mock_read_results):
        # Arrange
        races_location = ["Location1", "Location2", "Location3"]

        # Mock the behavior of read_integer_between_numbers
        mock_read_integer.return_value = 2  # Simulating the user selecting "Location2"

        # Mock the behavior of reading_race_results
        mock_read_results.return_value = (101, "2:45")  # Simulating ID and time

        # Act
        result = race_results(races_location)

        # Assert
        self.assertEqual(result, (101, "2:45", "Location2"))
        mock_read_integer.assert_called_once_with("Choice > ", 1, len(races_location))
        mock_read_results.assert_called_once_with("Location2")


if __name__ == '__main__':
    unittest.main()
