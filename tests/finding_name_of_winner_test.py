import unittest
from main import finding_name_of_winner


class TestFindingNameOfWinner(unittest.TestCase):

    def test_typical_case(self):
        """Test when the fastest_runner ID exists in runners_id."""
        fastest_runner = "ID3"
        runners_id = ["ID0", "ID1", "ID2", "ID3"]
        runners_name = ["Thomas", "Andrew", "Aj", "Luis"]
        self.assertEqual(finding_name_of_winner(fastest_runner, runners_id, runners_name), "Luis")

    def test_runner_not_found(self):
        """Test case when fastest_runner ID is not in runners_id its missing."""
        fastest_runner = "ID5"
        runners_id = ["ID0", "ID1", "ID2", "ID3"]
        runners_name = ["Thomas", "Andrew", "Aj", "Luis"]
        self.assertIsNone(finding_name_of_winner(fastest_runner, runners_id, runners_name))

    def test_empty_lists(self):
        """Test case when list is empty for runners_id and runners_name."""
        fastest_runner = "ID1"
        runners_id = []
        runners_name = []
        self.assertIsNone(finding_name_of_winner(fastest_runner, runners_id, runners_name))

    def test_multiple_occurrences(self):
        """Test case where fastest_runner ID appears multiple times in runners_id."""
        fastest_runner = "ID1"
        runners_id = ["ID0", "ID1", "ID2", "ID1"]
        runners_name = ["Thomas", "Andrew", "Aj", "Luis"]
        self.assertEqual(finding_name_of_winner(fastest_runner, runners_id, runners_name), "Andrew")


if __name__ == "__main__":
    unittest.main()
