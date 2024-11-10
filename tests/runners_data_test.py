
"""
Unit testing of the `extract_info_text` utils function
"""

# Imports

import unittest
from main import runners_data


# Tests

class AppTests(unittest.TestCase):

    def test_length(self):
        """
        Lengths
        """
        runners, ids = runners_data()

        # Both lists need the same length
        self.assertEqual(len(runners), len(ids))

        # Must not be empty
        self.assertGreater(len(runners), 0)

    def test_nonempty(self):
        """
        Not empty
        """
        runners, ids = runners_data()

        # Check if empty items in it
        self.assertFalse('' in runners)
        self.assertFalse('' in ids)
