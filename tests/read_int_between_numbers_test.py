import unittest
from main import read_integer_between_numbers
from unittest.mock import patch

class TestReadIntegerBetweenNumbers(unittest.TestCase):
    """
    Unit tests for the `read_integer_between_numbers` function.

    This class contains tests for the `read_integer_between_numbers` function, 
    which reads an integer input from the user within a specified range. 
    The tests cover scenarios for valid inputs, out-of-range inputs, 
    non-integer inputs, and multiple invalid inputs.
    """

    # Test when a valid input is provided
    @patch('builtins.input', side_effect=['5'])  # Use side_effect to simulate a single input
    def test_valid_input_within_range(self, mock_input):
        """
        Test case for when the input is a valid integer within the specified range.

        This test checks that the function correctly accepts a valid input (5 in this case)
        that lies within the given range (1 to 7).
        """
        result = read_integer_between_numbers("Enter a number", 1, 7)
        self.assertEqual(result, 5)  # Expect 5 to be returned since it's within the range

    # Test when the input is out of range (too low)
    @patch('builtins.input', side_effect=['0', '5'])  # First invalid, then valid input
    def test_input_below_range(self, mock_input):
        """
        Test case for when the input is below the specified range.

        This test simulates a user providing an input (0) that is too low, 
        and then a valid input (5). The function should reject the invalid input 
        and accept the valid one.
        """
        result = read_integer_between_numbers("Enter a number", 1, 7)
        self.assertEqual(result, 5)  # The valid input after the invalid one

    # Test when the input is out of range (too high)
    @patch('builtins.input', side_effect=['11', '5'])  # First invalid, then valid input
    def test_input_above_range(self, mock_input):
        """
        Test case for when the input is above the specified range.

        This test simulates a user providing an input (11) that is too high, 
        and then a valid input (5). The function should reject the invalid input 
        and accept the valid one.
        """
        result = read_integer_between_numbers("Enter a number", 1, 7)
        self.assertEqual(result, 5)  # The valid input after the invalid one

    # Test when input is non-integer
    @patch('builtins.input', side_effect=['abc', '3'])
    def test_non_integer_input(self, mock_input):
        """
        Test case for when the input is a non-integer.

        This test simulates a user providing an invalid input ('abc') 
        followed by a valid integer input (3). The function should reject the 
        non-integer input and accept the second valid input.
        """
        result = read_integer_between_numbers("Enter a number", 1, 7)
        self.assertEqual(result, 3)  # After invalid input, the second input should be accepted
    
    # Test multiple invalid inputs
    @patch('builtins.input', side_effect=['-1', 'abc', '3'])
    def test_multiple_invalid_inputs(self, mock_input):
        """
        Test case for multiple invalid inputs before a valid one.

        This test simulates the user entering a series of invalid inputs 
        (-1 and 'abc') before finally providing a valid input (3). 
        The function should keep prompting until a valid input is given.
        """
        result = read_integer_between_numbers("Enter a number", 1, 7)
        self.assertEqual(result, 3)  # The valid input is the third attempt

if __name__ == '__main__':
    unittest.main()
