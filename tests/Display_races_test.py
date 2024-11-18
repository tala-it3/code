import unittest
from unittest.mock import patch
from io import StringIO

# The function we want to test
from main import display_races

# Test case class
class TestDisplayRaces(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)  # Redirect print output
    def test_display_races(self, mock_stdout):
        # Define test input
        ids = ["Racer1", "Racer2", "Racer3"]
        times = [130, 90, 150]  # In seconds
        venue = "Main Stadium"
        fastest_runner = "Racer2"

        # Call the function
        display_races(ids, times, venue, fastest_runner)

        # Expected output
        expected_output = (
            "Results for Main Stadium\n"
            "=====================================\n"
            "Racer1     2 minutes and 30 seconds\n"
            "Racer2     1 minutes and 40 seconds\n"
            "Racer3     3 minutes and 0 seconds\n"
            "Racer2 won the race.\n"
        )

        # Check if the printed output matches the expected output
        self.assertEqual(mock_stdout.getvalue(), expected_output)

# Run the tests
if __name__ == '__main__':
    unittest.main()

