"""
Created on 10/03/2018
@author Stefan
"""
import copy

from Domain.CellInfo import CellInfo
from Domain.Exceptions import ReadFromFileException, IncorrectInputFileException
from Utils.Math import Math


class SudokuBoard:

    def __init__(self, previousBoard = None, cellsList = None, variant = None):
        self.__boardSize = 0
        self.__board = []

        if previousBoard is not None and cellsList is not None and variant is not None:
            self.__boardSize = copy.deepcopy(previousBoard.getBoardSize())
            self.__board = copy.deepcopy(previousBoard.getBoard())
            for index, cell in enumerate(cellsList):
                line = cell.getLine()
                column = cell.getColumn()
                self.__board[line][column].setCellNumber(cell.getPossibleDigits()[variant])
                self.__board[line][column].getPossibleDigits().clear()
                self.handleNewDigit(line, column, cell.getPossibleDigits()[variant])


    def getBoardSize(self):
        return self.__boardSize


    def getBoard(self):
        return self.__board


    def readFromFile(self, fileName):
        fileHandler = open(fileName, "r")
        fileContent = fileHandler.readlines()
        self.__boardSize = len(fileContent)

        if not Math.is_square(self.__boardSize):
            raise IncorrectInputFileException("Input file is not correct")

        for index in range(0, self.__boardSize):
            self.__board.append([])
            fileContent[index] = fileContent[index].split(" ")
            if len(fileContent[index]) != self.__boardSize:
                raise ReadFromFileException("Wrong input file.")
            for index2 in range(0, self.__boardSize):
                cellData = CellInfo(int(fileContent[index][index2]), index, index2, self.__boardSize)
                self.__board[index].append(cellData)

        for index in range(0, self.__boardSize):
            for index2 in range(0, self.__boardSize):
                if self.__board[index][index2].getCellNumber() == 0:
                    self.__board[index][index2].setPossibleDigits(self.getAvailableDigitsForCell(index, index2))
                else:
                    self.__board[index][index2].getPossibleDigits().clear()


    def handleNewDigit(self, line, column, number):
        for index in range(0, self.__boardSize):
            self.__board[line][index].removePossibility(number)
        for index in range(0, self.__boardSize):
            self.__board[index][column].removePossibility(number)
        squareSize = Math.isqrt(self.__boardSize)
        squareTopLine = (line//squareSize)*squareSize
        squareLeftColumn = (column//squareSize)*squareSize
        for index1 in range(squareTopLine, squareTopLine + squareSize):
            for index2 in range(squareLeftColumn, squareLeftColumn + squareSize):
                self.__board[index1][index2].removePossibility(number)


    def getNextConfiguration(self, cellsToComplete, numberOfPossibilities, variant = 0):
        if numberOfPossibilities == 1:
            return SudokuBoard(self, cellsToComplete, variant)
        else:
            return SudokuBoard(self, cellsToComplete, variant)


    # gets the numbers already in the square containing that line and column
    def getSquareNumbers(self, line, column):
        numbers = []
        squareSize = Math.isqrt(self.__boardSize)
        squareTopLine = (line//squareSize)*squareSize
        squareLeftColumn = (column//squareSize)*squareSize
        for index1 in range(squareTopLine, squareTopLine + squareSize):
            for index2 in range(squareLeftColumn, squareLeftColumn + squareSize):
                numbers.append(self.__board[index1][index2].getCellNumber())
        return numbers


    def getNumbersOnLine(self, line):
        numbers = []
        for index in range(0,self.__boardSize):
            numbers.append(self.__board[line][index].getCellNumber())
        return numbers


    def getNumbersOnColumn(self, column):
        numbers = []
        for index in range(0,self.__boardSize):
            numbers.append(self.__board[index][column].getCellNumber())
        return numbers


    def getAvailableDigitsForCell(self, line, column):
        missingNumbers = []
        squareNumbers = self.getSquareNumbers(line, column)
        lineNumbers = self.getNumbersOnLine(line)
        columnNumbers = self.getNumbersOnColumn(column)
        for number in range(1,self.__boardSize + 1):
            if number not in lineNumbers and number not in columnNumbers and number not in squareNumbers:
                missingNumbers.append(number)
        return missingNumbers


    ## creates a list of objects containing line, column and possible entries for that cell, all objects will be with one possibility, or just a cell with more than 1.
    def getNextSetOfCells(self):
        cellSet = []
        for index in range(0, self.__boardSize):
            for index2 in range(0, self.__boardSize):
                if len(self.__board[index][index2].getPossibleDigits()) == 1:
                    cellSet.append(copy.deepcopy(self.__board[index][index2]))
        if len(cellSet) != 0:
            return cellSet
        else:
            for index in range(0, self.__boardSize):
                for index2 in range(0, self.__boardSize):
                    if len(self.__board[index][index2].getPossibleDigits()) != 0:
                        cellToReturn = copy.deepcopy(self.__board[index][index2])
                        return [cellToReturn]


    def getDigitCount(self):
        digits = [0,0,0,0,0,0,0,0,0,0]
        for index in range(0, self.__boardSize):
            for index2 in range(0, self.__boardSize):
                digits[self.__board[index][index2].getCellNumber()] += 1
        return digits


    def isComplete(self):
        for index in range(0, self.__boardSize):
            if 0 in self.getNumbersOnColumn(index):
                return False
        return True


    def __str__(self):
        s = ""
        for index in range(0, self.__boardSize):
            for index2 in range(0, self.__boardSize):
                s += str(self.__board[index][index2]) + " "
            s += "\n"
        return s
