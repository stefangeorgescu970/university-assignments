"""
Created on 08/04/2018
@author Stefan
"""

class Velocity:
    def __init__(self, xChange = 0, yChange = 0):
        self.__xChange = xChange
        self.__yChange = yChange

    @property
    def xChange(self):
        return self.__xChange

    @xChange.setter
    def xChange(self, value):
        self.__xChange = value

    @property
    def yChange(self):
        return self.__yChange

    @yChange.setter
    def yChange(self, value):
        self.__yChange = value