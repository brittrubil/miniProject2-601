from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.Multiplication import multiplication


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def div(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiple(self, a, b):
        self.result = multiplication(a, b)
        return self.result


