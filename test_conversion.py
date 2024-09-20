import unittest
import pandas as pd
from data_transformation import convert_duration

class TestDataIngestion(unittest.TestCase):
    def test_duration_conversion(self):
        """Test the conversion of duration field to seconds."""
        sample_data = {
            'trip_id': [1, 2, 3],
            'duration': ['00:30:00', '01:15:30', "1.18:28:20.1269999"] #Input Durations
        }
        df = pd.DataFrame(sample_data)
        df["duration_seconds"] = df["duration"].apply(lambda x: convert_duration(x)) #Applying conversion function
        expected_durations = [1800.0, 4530.0, 152900.1269999]  # Expected duration in seconds
        actual_durations = df["duration_seconds"].tolist()
        self.assertEqual(expected_durations, actual_durations)

if __name__ == '__main__':
    unittest.main()