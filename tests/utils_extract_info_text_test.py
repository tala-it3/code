
"""
Unit testing of the `extract_info_text` utils function
"""

# Imports

import unittest
from utils import extract_info_text


# Tests

class AppTests(unittest.TestCase):

    def test_pass(self):
        """
        Simple Tests
        """
        self.assertEqual(extract_info_text("a,b\nc,d"), [['a', 'b'], ['c', 'd']])
        self.assertEqual(extract_info_text("a#b\nc#d", separator='#'), [['a', 'b'], ['c', 'd']])
        self.assertEqual(extract_info_text("a,  b\n  c,  d ", clear=True), [['a', 'b'], ['c', 'd']])
        self.assertNotEqual(extract_info_text("a,b\nc,d"), ['a', 'b', 'c', 'd'])

    def test_errors(self):
        """
        Check if we raise errors
        """
        with self.assertRaises(TypeError):
            extract_info_text(12)

        with self.assertRaises(TypeError):
            extract_info_text(False)

        with self.assertRaises(TypeError):
            extract_info_text([])

        with self.assertRaises(TypeError):
            extract_info_text({})

        with self.assertRaises(TypeError):
            extract_info_text(False, False)

        with self.assertRaises(TypeError):
            extract_info_text([], {})

        with self.assertRaises(TypeError):
            extract_info_text({}, "")
