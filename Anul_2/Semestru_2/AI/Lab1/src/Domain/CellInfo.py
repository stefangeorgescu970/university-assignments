"""
Created on 14/03/2018
@author Stefan
"""

class CellInfo:

    def __init__(self, number, line, column, boardSize):
        self.__number = number
        self.__line = line
        self.__column = column
        self.__possibleDigits = list(range(1, boardSize+1))
        if number != 0:
            self.__possibleDigits.remove(number)

    def getPossibleDigits(self):
        return self.__possibleDigits

    def setPossibleDigits(self, list):
        self.__possibleDigits = list

    def removePossibility(self, digit):
        if digit in self.__possibleDigits:
            self.__possibleDigits.remove(digit)

    def getCellNumber(self):
        return self.__number

    def setCellNumber(self, number):
        self.__number = number

    def getLine(self):
        return self.__line

    def getColumn(self):
        return self.__column

    def __str__(self):
        return str(self.__number)