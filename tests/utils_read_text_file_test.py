
"""
Unit testing of the `read_text_file` utils function
"""

# Imports

import os.path
import unittest
from utils import read_text_file

# Get current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
def file_here(path): return str(os.path.join(current_directory, path))


# Tests

class AppTests(unittest.TestCase):

    def test_pass(self):
        """
        Simple Tests
        """
        self.assertEqual(read_text_file(file_here("utils_read_text_file_test.txt"), clear=False), "Sample\n\nEnd")
        self.assertEqual(read_text_file(file_here("utils_read_text_file_test.txt"), clear=True), "Sample\nEnd")
        self.assertNotEqual(read_text_file(file_here("utils_read_text_file_test.txt"), clear=True), "Sample\n\nEnd")

    def test_errors(self):
        """
        Check if we raise errors
        """
        with self.assertRaises(TypeError):
            read_text_file(12)
            read_text_file(False)
            read_text_file([])
            read_text_file({})


def suite():
    _suite = unittest.TestSuite()
    _suite.addTest(AppTests('test_errors'))
    _suite.addTest(AppTests('test_pass'))
    return _suite
