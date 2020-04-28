"""
Created on 10/03/2018
@author Stefan
"""


class State:
    '''
    holds a PATH of Sudoku Boards that will contribute to a solution
    '''
    def __init__(self):
        self.__values = []

    def setValues(self, values):
        self.__values = values[:]

    def getValues(self):
        return self.__values[:]

    def __str__(self):
        s=''
        for x in self.__values:
            s+=str(x)+"\n"
        return s

    def __add__(self, board):
        aux = State()
        aux.setValues(self.__values+[board])
        return aux