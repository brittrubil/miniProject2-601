from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Deviation import deviation
from Statistics.Proportion import proportion
from Statistics.Zscore import zscore
from Statistics.StandardScore import standardscore


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

    def proportion(self, a, b, c):
        self.result = proportion(a, b, c)
        return self.result

    def zscore(self, a, b, c):
        self.result = zscore(a, b, c)
        return self.result

    def standardscore(self, a, b, c):
        self.result = standardscore(a, b, c)
        return self.result

