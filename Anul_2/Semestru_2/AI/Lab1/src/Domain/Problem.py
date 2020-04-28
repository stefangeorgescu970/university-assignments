"""
Created on 10/03/2018
@author Stefan
"""
from Domain.State import State
from Utils.Math import Math


class Problem:

    def __init__(self, initial):
        self.__initialConfig = initial
        self.__initialState = State()
        self.__initialState.setValues([self.__initialConfig])

    def getRoot(self):
        return self.__initialState

    def expand(self, currentState):
        myList = []
        currentConfig = currentState.getValues()[-1]

        cellsToComplete = currentConfig.getNextSetOfCells()
        if cellsToComplete is not None:
            numberOfPossibilities = len(cellsToComplete[0].getPossibleDigits())
            if len(cellsToComplete) > 1 :
                nextConfig = currentConfig.getNextConfiguration(cellsToComplete, numberOfPossibilities)
                if nextConfig is not None:
                    myList.append(currentState+nextConfig)
            else:
                for index, cell in enumerate(cellsToComplete[0].getPossibleDigits()):
                    nextConfig = currentConfig.getNextConfiguration(cellsToComplete, numberOfPossibilities, index)
                    if nextConfig is not None:
                        myList.append(currentState+nextConfig)
        return myList

    def heuristics(self, state, previousState):
        """
        priority for the state which adds more digits of the one that is present the least
        :param state: the current state
        :param previousState: the previous state
        :return: how many digits of the least present one appear
        """
        digitsNow = state.getValues()[-1].getDigitCount()
        digitsThen = previousState.getValues()[-1].getDigitCount()

        minDigit = min(digitsThen)
        return digitsNow[minDigit] - digitsThen[minDigit]