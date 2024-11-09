import unittest
from unittest.mock import patch
from main import read_integer

class TestReadInteger(unittest.TestCase):
    """
    Unit tests for the read_integer function, which prompts the user for a non-negative 
    integer input, handling and retrying on invalid inputs. This test suite uses mock input to 
    simulate various user input scenarios, including valid and invalid cases.
    """

    @patch('builtins.input', side_effect=['-5', '3'])
    def test_negative_input(self, mock_input):
        """
        Test if a negative integer input is rejected and the user is prompted again.
        
        This test simulates an initial input of -5, which should be rejected by the function.
        The function should then prompt again and accept the next input of 3, which is a 
        valid non-negative integer.
        """
        result = read_integer("Enter an integer: ")
        self.assertEqual(result, 3)  # Expects the first valid non-negative integer (3)

    @patch('builtins.input', side_effect=['abc', '5'])
    def test_string_input(self, mock_input):
        """
        Test if a non-integer string input is rejected and the user is prompted again.
        
        This test simulates an initial input of 'abc', which is an invalid string.
        The function should prompt again, and the second input of 5 should be accepted as 
        a valid integer.
        """
        result = read_integer("Enter an integer: ")
        self.assertEqual(result, 5)  # Expects 5 after invalid string input

    @patch('builtins.input', side_effect=['4.5', '7'])
    def test_float_input(self, mock_input):
        """
        Test if a float input is rejected and the user is prompted again.
        
        This test simulates an initial input of 4.5, which is a float and should be rejected.
        The function should then prompt again, and the second input of 7 should be accepted 
        as a valid integer.
        """
        result = read_integer("Enter an integer: ")
        self.assertEqual(result, 7)  # Expects 7 after invalid float input

    @patch('builtins.input', side_effect=['', '2'])
    def test_empty_input(self, mock_input):
        """
        Test if an empty input is rejected and the user is prompted again.
        
        This test simulates an empty input ('') initially, which should be rejected. 
        The function should prompt again, and the second input of 2 should be accepted 
        as a valid integer.
        """
        result = read_integer("Enter an integer: ")
        self.assertEqual(result, 2)  # Expects 2 after empty input

    @patch('builtins.input', side_effect=['10'])
    def test_valid_input(self, mock_input):
        """
        Test if a valid integer input is accepted on the first attempt.
        
        This test simulates an input of 10, which is a valid non-negative integer and 
        should be accepted immediately without prompting again.
        """
        result = read_integer("Enter an integer: ")
        self.assertEqual(result, 10)  # Expects 10 as a valid integer input

if __name__ == "__main__":
    unittest.main()
