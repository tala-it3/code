import unittest
from unittest.mock import patch


class TestDisplayingRunnersWhoHaveWonAtLeastOneRace(unittest.TestCase):

    @patch('main.reading_race_results', return_value=([101], [10.5]))
    @patch('main.winner_of_race', return_value=101)
    @patch('main.finding_name_of_winner', return_value="Runner A")
    def test_single_race(self, mock_finding_name, mock_winner, mock_results):
        # Test inputs
        races_location = ["location1"]
        runners_name = ["Runner A"]
        runners_id = [101]

        # Expected output
        expected_output = (
            "The following runners have all won at least one race:\n"
            "-------------------------------------------------------\n"
            "Runner A (101)\n"
        )

        # Capture printed output
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function
        from main import displaying_runners_who_have_won_at_least_one_race
        displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)




if __name__ == '__main__':
    unittest.main()

