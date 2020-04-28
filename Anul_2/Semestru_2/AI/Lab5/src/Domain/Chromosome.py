"""
Created on 19/05/2018
@author Stefan
"""
from random import random, randint

from Utils.AppConstants import AppConstants


class Chromosome:
    def __init__(self, depth=AppConstants.DEPTH_MAX):
        self.maximumDepth = depth
        self.representation = [0 for i in range(2 ** (self.maximumDepth + 1) - 1)]
        self.fitness = 0
        self.size = 0

    def initialise(self):
        self.growExpression()

    def initialiseFull(self):
        numberOfFunctions = 2 ** self.maximumDepth - 1
        for index in range(numberOfFunctions):
            self.representation[index] = -randint(1, AppConstants.NUMBER_OF_FUNCTIONS)
        for index in range(numberOfFunctions, 2 ** (self.maximumDepth + 1) - 1):
            self.representation[index] = randint(1, AppConstants.NUMBER_OF_TERMINALS)

    def growExpression(self, pos=0, depth=0):
        if (pos == 0) or (depth < self.maximumDepth):
            if random() < 0.3:
                self.representation[pos] = randint(1, AppConstants.NUMBER_OF_TERMINALS)
                self.size = pos + 1
                return pos + 1
            else:
                self.representation[pos] = -randint(1, AppConstants.NUMBER_OF_FUNCTIONS)
                finalFirstChild = self.growExpression(pos + 1, depth + 1)
                finalSecondChild = self.growExpression(finalFirstChild, depth + 1)
                return finalSecondChild
        else:
            self.representation[pos] = randint(1, AppConstants.NUMBER_OF_TERMINALS)
            self.size = pos + 1
            return pos + 1

    def evalExpression(self, pos, dataRow):
        if self.representation[pos] > 0:  # a terminal
            return dataRow[self.representation[pos] - 1], pos
        elif self.representation[pos] == 0:
            return 1, pos
        elif self.representation[pos] < 0:  # a function
            if AppConstants.FUNCTIONS[-self.representation[pos] - 1] == '+':
                auxFirst = self.evalExpression(pos + 1, dataRow)
                auxSecond = self.evalExpression(auxFirst[1] + 1, dataRow)
                return auxFirst[0] + auxSecond[0], auxSecond[1]
            elif AppConstants.FUNCTIONS[-1 - self.representation[pos]] == '-':
                auxFirst = self.evalExpression(pos + 1, dataRow)
                auxSecond = self.evalExpression(auxFirst[1] + 1, dataRow)
                return auxFirst[0] - auxSecond[0], auxSecond[1]
            elif AppConstants.FUNCTIONS[-1 - self.representation[pos]] == '*':
                auxFirst = self.evalExpression(pos + 1, dataRow)
                auxSecond = self.evalExpression(auxFirst[1] + 1, dataRow)
                return auxFirst[0] * auxSecond[0], auxSecond[1]
            elif AppConstants.FUNCTIONS[-1 - self.representation[pos]] == '/':
                auxFirst = self.evalExpression(pos + 1, dataRow)
                auxSecond = self.evalExpression(auxFirst[1] + 1, dataRow)
                return auxFirst[0] * auxSecond[0], auxSecond[1]

    def computeFitness(self, dataCluster):
        err = 0.0
        for d in range(dataCluster.getNumberOfRows()):
            err += abs(dataCluster.dataRows[d].expectedOutput - self.evalExpression(0, dataCluster.dataRows[d])[0])
        self.fitness = err

    def traverse(self, pos):
        if self.representation[pos] >= 0:  # terminal
            return pos + 1
        else:
            return self.traverse(self.traverse(pos + 1))

    def mutate(self):
        pos = randint(0, self.size - 1)

        if self.representation[pos] > 0:  # terminal
            self.representation[pos] = randint(1, AppConstants.NUMBER_OF_TERMINALS)
        else:  # function
            self.representation[pos] = -randint(1, AppConstants.NUMBER_OF_FUNCTIONS)
