import unittest
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()


    def test_mean(self):
        test_data = CsvReader("/Tests/Data/Mean.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.mean(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.statistics.result, float(row['Result']))



if __name__ == '__main__':
    unittest.main()