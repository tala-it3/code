import unittest
from unittest.mock import patch

# Import your `race_results` function, `read_integer_between_numbers`, and `reading_race_results`.
# Replace `your_module` with the actual name of your module.
from main import race_results, read_integer_between_numbers, reading_race_results


class TestRaceResults(unittest.TestCase):
    @patch('your_module.reading_race_results')  # Mock the `reading_race_results` function
    @patch('your_module.read_integer_between_numbers')  # Mock the `read_integer_between_numbers` function
    def test_race_results(self, mock_read_integer, mock_read_results):
        # Arrange
        races_location = ["Location1", "Location2", "Location3"]

        # Mocking behavior of `read_integer_between_numbers`
        mock_read_integer.return_value = 2  # Simulate user selecting "Location2"

        # Mocking behavior of `reading_race_results`
        mock_read_results.return_value = (101, "2:45")  # Simulate returning ID and time

        # Act
        result = race_results(races_location)

        # Assert
        self.assertEqual(result, (101, "2:45", "Location2"))  # Verify the returned value is as expected
        mock_read_integer.assert_called_once_with("Choice > ", 1,
                                                  len(races_location))  # Verify the input function is called correctly
        mock_read_results.assert_called_once_with(
            "Location2")  # Verify the results function is called with the correct location


if __name__ == '__main__':
    unittest.main()
