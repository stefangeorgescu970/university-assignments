"""
Created on 31/05/2018
@author Stefan
"""


class LFunctionData:
    def __init__(self, leftValue, tipValue):
        self.__leftValue = leftValue
        self.__tipValue = tipValue

    def getFunctionValueFor(self, number):
        if number < self.__leftValue:
            return 0
        if number > self.__tipValue:
            return 1
        return (number - self.__leftValue) / (self.__tipValue - self.__leftValue)

    def getTipValue(self):
        return self.__tipValue