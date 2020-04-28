"""
Created on 31/05/2018
@author Stefan
"""


class RFunctionData:
    def __init__(self, tipValue, rightValue):
        self.__tipValue = tipValue
        self.__rightValue = rightValue

    def getFunctionValueFor(self, number):
        if number > self.__rightValue:
            return 0
        if number < self.__tipValue:
            return 1
        return (self.__rightValue - number) / (self.__rightValue - self.__tipValue)

    def getTipValue(self):
        return self.__tipValue