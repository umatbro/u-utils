import pandas as pd
import unittest
import um.statistics as stats


class TestStatistics(unittest.TestCase):
    def test_filter_outliers_in_series(self):
        data = pd.Series([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1000])
        filtered_data = stats.filter_outliers(data)
        self.assertTrue(pd.Series([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]).equals(filtered_data))
        self.assertEqual(filtered_data.mean(), 2)

    def test_leave_all_data_in_series_when_no_outliers(self):
        # mean: 7.555, std: 5,57
        data = pd.Series([5, 9, 3, 10, -2, 6, 12, 17, 8])

        filtered_data = stats.filter_outliers(data, 2)
        self.assertTrue(data.equals(filtered_data))
