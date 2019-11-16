from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Deviation import deviation
from Statistics.Variance import variance
from Statistics.Zscore import zscore
from Statistics.Proportion import proportion
from Statistics.Pvalue import pvalue
from Statistics.StandardScore import standardscore
from Statistics.Correlation_Coefficient import correlation_coefficient
from Statistics.Confidence_Interval import confidence_interval



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

    def correlation_coefficient(self, a):
        self.result = correlation_coefficient(a)
        return self.result

    def confidence_interval(self, a):
        self.result = confidence_interval(a)
        return self.result

    def pvariance(self, a, b, c, d, e, f, g, h):
        self.result = variance(a, b, c, d, e, f, g, h)
        return self.result

    def pvalue(self, a, b, c, d):
        self.result = pvalue(a, b, c, d)
        return self.result