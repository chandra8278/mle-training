import unittest
import os
from src import fetch_housing_data, load_housing_data


class TestHousingLibraryFunctional(unittest.TestCase):
    def test_fetch_housing_data(self):
        housing_path = 'datasets/housing'
        fetch_housing_data(housing_path)

        # Check if the housing.csv file exists
        csv_path = os.path.join(housing_path, "housing.csv")
        self.assertTrue(os.path.isfile(csv_path))

    def test_load_housing_data(self):
        housing_data = load_housing_data()
        self.assertIsNotNone(housing_data)
        self.assertEqual(housing_data.shape, (20640, 10))

    def test_fetch_and_load_housing_data(self):
        fetch_housing_data()
        load_housing_data()
        # Perform test assertions to validate the fetched and loaded data
        pass


if __name__ == '__main__':
    unittest.main()
