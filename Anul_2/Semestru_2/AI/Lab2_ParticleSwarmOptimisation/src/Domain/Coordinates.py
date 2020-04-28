"""
Created on 08/04/2018
@author Stefan
"""

class Coordinates:

    def __init__(self, xPosition, yPosition):
        self.__xPosition = xPosition
        self.__yPosition = yPosition

    @property
    def xPosition(self):
        return self.__xPosition

    @xPosition.setter
    def xPosition(self, value):
        self.__xPosition = value

    @property
    def yPosition(self):
        return self.__yPosition

    @yPosition.setter
    def yPosition(self, value):
        self.__yPosition = value
