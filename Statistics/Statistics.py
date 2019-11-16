from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Deviation import deviation

class Statistics:
    data = []

    def mean(self, a, b):
        self.result = mean(a, b)
        return self.result

    def median(self, a, b, c, d):
        self.result = median(a, b, c, d)
        return self.result

    def mode(self, a, b, c, d):
        self.result = mode(a, b, c, d)
        return self.result

    def stdev(self, a, b, c, d, e):
        self.result = deviation(a, b, c, d, e)
        return self.result