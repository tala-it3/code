import unittest
from main import winner_of_race

class TestWinnerOfRace(unittest.TestCase):
    
    def test_basic_case(self):
        # Test with a typical set of participants and times.
        ids = ['A', 'B', 'C', 'D']
        times = [10, 20, 5, 15]
        self.assertEqual(winner_of_race(ids, times), 'C')

    def test_ignore_zero_times(self):
        # Test that participants with time zero are ignored.
        ids = ['A', 'B', 'C', 'D']
        times = [0, 20, 5, 15]
        self.assertEqual(winner_of_race(ids, times), 'C')

    def test_all_zero_times(self):
        # Test case where all times are zero
        ids = ['A', 'B', 'C', 'D']
        times = [0, 0, 0, 0]
        # should return an empty string.
        self.assertEqual(winner_of_race(ids, times), "")

    def test_tie_for_first_place(self):
        # Test case where two participants have the same shortest time.
        ids = ['A', 'B', 'C', 'D']
        times = [10, 5, 5, 15]
        self.assertEqual(winner_of_race(ids, times), 'B')
