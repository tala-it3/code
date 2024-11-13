import unittest
from main import competitors_by_county
from unittest.mock import patch
from io import StringIO

class TestCompetitorsByCounty(unittest.TestCase):
    # Test for normal input with multiple counties
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiple_counties(self, mock_stdout):
        names = ['Alice', 'Bob', 'Charlie', 'David']
        ids = ['NY-001', 'NY-002', 'CA-001', 'CA-002']

        competitors_by_county(names, ids)

        expected_output = (
            "CA runners\n"
            "====================\n"
            "Charlie (CA-001)\n"
            "David (CA-002)\n\n"
            "NY runners\n"
            "====================\n"
            "Alice (NY-001)\n"
            "Bob (NY-002)\n\n"
        )
        
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # check if the function handles multiple competitors in the same county properly, sorting by name.
    @patch('sys.stdout', new_callable=StringIO)
    def test_equal_names_in_same_county(self, mock_stdout):
        names = ['Alice', 'Bob', 'Charlie', 'David', 'Alice']
        ids = ['NY-001', 'NY-002', 'CA-001', 'CA-002', 'NY-003']

        competitors_by_county(names, ids)

        expected_output = (
            "CA runners\n"
            "====================\n"
            "Charlie (CA-001)\n"
            "David (CA-002)\n\n"
            "NY runners\n"
            "====================\n"
            "Alice (NY-001)\n"
            "Alice (NY-003)\n"
            "Bob (NY-002)\n\n"
        )
        
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Test for error case when names and IDs lists have different lengths
    @patch('sys.stdout', new_callable=StringIO)
    def test_different_lengths(self, mock_stdout):
        names = ['Alice', 'Bob']
        ids = ['NY-001']

        competitors_by_county(names, ids)

        expected_output = "Error: Name and ID lists must have the same length.\n"
        
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Test for empty input lists
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_input(self, mock_stdout):
        names = []
        ids = []

        competitors_by_county(names, ids)

        expected_output = ""
        
        self.assertEqual(mock_stdout.getvalue(), expected_output)