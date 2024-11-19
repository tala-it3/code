import unittest
from unittest.mock import patch
import os
from main import reading_race_results


class TestReadingRaceResults(unittest.TestCase):

    def test_reading_race_results_valid_data(self):
        """Test reading valid race results."""
        def mock_read_text_file(filepath):
            # Check that the correct file path is constructed
            expected_path = os.path.join("/fake/path", "blarney.txt")
            self.assertEqual(filepath, expected_path)
            return "mock file content"

        def mock_extract_info_text(file_content, separator):
            # Check that the content and separator are correct
            self.assertEqual(file_content, "mock file content")
            self.assertEqual(separator, ',')
            return [
                ['KY-43', '1915'],
                ['CK-11', '2045'],
                ['CK-23', '2020'],
                ['WD-32', '1928'],
            ]

        with patch('main.config.INFO_FOLDER', "/fake/path"):
            with patch('main.utils.read_text_file', side_effect=mock_read_text_file):
                with patch('main.utils.extract_info_text', side_effect=mock_extract_info_text):
                    # Call the function
                    runner_ids, times = reading_race_results("blarney")

                    # Assert results
                    self.assertEqual(runner_ids, ['KY-43', 'CK-11', 'CK-23', 'WD-32'])
                    self.assertEqual(times, [1915, 2045, 2020, 1928])

    def test_file_not_found(self):
        """Test behavior when the file does not exist."""
        def mock_read_text_file(filepath):
            # Simulate a file not found error
            raise FileNotFoundError

        with patch('main.config.INFO_FOLDER', "/fake/path"):
            with patch('main.utils.read_text_file', side_effect=mock_read_text_file):
                # Expect FileNotFoundError to be raised
                with self.assertRaises(FileNotFoundError):
                    reading_race_results("nonexistent_location")

    def test_invalid_data_format(self):
        """Test behavior with improperly formatted data."""
        def mock_read_text_file(filepath):
            return "mock file content"

        def mock_extract_info_text(file_content, separator):
            # Simulate invalid data
            return [
                ['KY-43', '1915'],  # Valid row
                ['CK-11'],          # Missing time
                ['InvalidRow']      # Completely invalid row
            ]

        with patch('main.config.INFO_FOLDER', "/fake/path"):
            with patch('main.utils.read_text_file', side_effect=mock_read_text_file):
                with patch('main.utils.extract_info_text', side_effect=mock_extract_info_text):
                    # Expect ValueError to be raised
                    with self.assertRaises(ValueError):
                        reading_race_results("blarney")

    def test_empty_file(self):
        """Test behavior with an empty file."""
        def mock_read_text_file(filepath):
            return ""

        def mock_extract_info_text(file_content, separator):
            # Simulate an empty file by returning an empty list
            return []

        with patch('main.config.INFO_FOLDER', "/fake/path"):
            with patch('main.utils.read_text_file', side_effect=mock_read_text_file):
                with patch('main.utils.extract_info_text', side_effect=mock_extract_info_text):
                    # Call the function
                    runner_ids, times = reading_race_results("empty_location")

                    # Assert results
                    self.assertEqual(runner_ids, [])
                    self.assertEqual(times, [])


if __name__ == "__main__":
    unittest.main()
