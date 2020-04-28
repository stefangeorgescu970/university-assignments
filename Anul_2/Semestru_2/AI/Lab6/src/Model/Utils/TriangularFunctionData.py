"""
Created on 31/05/2018
@author Stefan
"""


class TriangularFunctionData:
    def __init__(self, leftValue, tipValue, rightValue):
        self.__leftValue = leftValue
        self.__tipValue = tipValue
        self.__rightValue = rightValue

    def getFunctionValueFor(self, number):
        if number <= self.__leftValue or number >= self.__rightValue:
            return 0
        if self.__leftValue < number <= self.__tipValue:
            return (number - self.__leftValue) / (self.__tipValue - self.__leftValue)
        return (self.__rightValue - number) / (self.__rightValue - self.__tipValue)

    def getTipValue(self):
        return self.__tipValue