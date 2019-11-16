from Statistics.Mean import mean
from Statistics.Median import median


class Statistics:
    data = []

    def mean(self, a, b):
        self.result = mean(a, b)
        return self.result

    def median(self, a, b, c, d):
        self.result = median(a, b, c, d)
        return self.result