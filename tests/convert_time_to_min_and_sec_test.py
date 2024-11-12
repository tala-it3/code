import unittest
from main import convert_time_to_minutes_and_seconds



# Unit test class
class TestConvertTimeToMinutesAndSeconds(unittest.TestCase):

    def test_simple_conversion(self):
        """Test a general case where time is a mix of minutes and seconds."""
        self.assertEqual(convert_time_to_minutes_and_seconds(125), (2, 5))

    def test_exact_minute(self):
        """Test the case where time is exactly one minute."""
        self.assertEqual(convert_time_to_minutes_and_seconds(60), (1, 0))

    def test_zero_seconds(self):
        """Test the case where time is zero."""
        self.assertEqual(convert_time_to_minutes_and_seconds(0), (0, 0))

    def test_less_than_minute(self):
        """Test the case where time is less than a minute."""
        self.assertEqual(convert_time_to_minutes_and_seconds(45), (0, 45))

    def test_multiple_minutes(self):
        """Test the case where time is multiple minutes exactly."""
        self.assertEqual(convert_time_to_minutes_and_seconds(360), (6, 0))

    def test_large_number(self):
        """Test the case where time is a large number."""
        self.assertEqual(convert_time_to_minutes_and_seconds(7265), (121, 5))




# Run the unit tests
if __name__ == "__main__":
    unittest.main()
