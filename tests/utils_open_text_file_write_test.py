
"""
Unit testing of the `read_text_file` utils function
"""

# Imports

import os
import unittest
from utils import (open_text_file_write,
                   read_text_file)

# Get current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
def file_here(path): return str(os.path.join(current_directory, path))


# Tests

class AppTests(unittest.TestCase):

    test_file = "__test.txt"
    test_data = "this is a test string\n"

    def test_pass(self):
        """
        Simple Tests
        """

        # Write file
        with open_text_file_write(file_here(self.test_file), False) as file:
            print(self.test_data, end='', file=file)

        # Test written file
        self.assertEqual(
            read_text_file(file_here(self.test_file), False),
            self.test_data
        )

        # Append file
        with open_text_file_write(file_here(self.test_file)) as file:
            print(self.test_data, end='', file=file)

        # Test written file
        self.assertEqual(
            read_text_file(file_here(self.test_file), False),
            self.test_data * 2
        )

        # Overwrite file
        with open_text_file_write(file_here(self.test_file), False) as file:
            print(self.test_data, end='', file=file)

        # Test written file
        self.assertEqual(
            read_text_file(file_here(self.test_file), False),
            self.test_data
        )

        # Remove the file
        os.remove(file_here(self.test_file))

    def test_errors(self):
        """
        Check if we raise errors
        """
        
        with self.assertRaises(TypeError):
            open_text_file_write(None)

        with self.assertRaises(TypeError):
            open_text_file_write(12)
