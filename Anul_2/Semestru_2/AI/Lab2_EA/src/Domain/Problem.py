"""
Created on 26/03/2018
@author Stefan
"""
from math import sin
from random import random

from Domain.Exception import AppException
from Domain.Individual import Individual
from Utils.AppConstants import AppConstants


class Problem:

    __xMinimalValue = None
    __xMaximalValue = None
    __yMinimalValue = None
    __yMaximalValue = None

    def __init__(self):
        self.readParameters(AppConstants.PROBLEM_PARAMETERS_FILE)

    def readParameters(self, fileName):
        fileHandler = open(fileName, "r")
        fileContent = fileHandler.readlines()
        fileContent = [x.strip() for x in fileContent]
        for line in fileContent:
            line = line.split(":")
            if line[0].strip() == AppConstants.X_MINIMUM_VALUE:
                self.__xMinimalValue = float(line[1].strip())
            elif line[0].strip() == AppConstants.X_MAXIMAL_VALUE:
                self.__xMaximalValue = float(line[1].strip())
            elif line[0].strip() == AppConstants.Y_MINIMAL_VALUE:
                self.__yMinimalValue = float(line[1].strip())
            elif line[0].strip() == AppConstants.Y_MAXIMAL_VALUE:
                self.__yMaximalValue = float(line[1].strip())
            else:
                raise AppException("Faulty parameters file.")

    def generateIndividual(self):
        xValue = (random() * (self.__xMaximalValue - self.__xMinimalValue) + self.__xMinimalValue)
        yValue = (random() * (self.__yMaximalValue - self.__yMinimalValue) + self.__yMinimalValue)
        return Individual(xValue, yValue)

    @staticmethod
    def computeFunctionValue(x, y):
        return sin(x+y) + (x-y)**2 - 1.5*x + 2.5*y + 1
