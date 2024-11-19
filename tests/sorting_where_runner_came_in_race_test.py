import unittest
import os
from main import sorting_where_runner_came_in_race


class TestSortingWhereRunnerCameInRace(unittest.TestCase):
    def setUp(self):
        # Create a temporary test file to see if time is in it or not
        self.test_file_name = "test_location.txt"
        with open(self.test_file_name, "w") as file:
            file.write("John,120\n")
            file.write("Doe,115\n")
            file.write("Smith,130\n")
            file.write("Jane,110\n")

    def tearDown(self):
        # Remove temporay test file after use
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    def test_sorting_where_runner_came_in_race(self):
        # Test the function with a given time that is in file
        position, total_runners = sorting_where_runner_came_in_race("test_location", 115)
        self.assertEqual(position, 2)  # Doe should be the 2nd in sorted order
        self.assertEqual(total_runners, 4)  # Total number of runners is 4

    def test_time_not_in_list(self):
        # Test the function with a time that doesn't exist in the file
        with self.assertRaises(ValueError):
            sorting_where_runner_came_in_race("test_location", 100)
