"""
Created on 08/04/2018
@author Stefan
"""
from Domain.Controller import Controller
from Domain.Exception import AppException
from Utils.AppConstants import AppConstants
import matplotlib.pyplot as plt

class Problem:

    __xMinimalValue = None
    __xMaximalValue = None
    __yMinimalValue = None
    __yMaximalValue = None

    def __init__(self):
        self.readParameters(AppConstants.PROBLEM_PARAMETERS_FILE)
        self.__controller = Controller(self.__xMinimalValue, self.__xMaximalValue, self.__yMinimalValue, self.__yMaximalValue)

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

    def run(self):
        bestIndividual = self.__controller.runAlgorithm()
        print('Result: The detected minimum point is (%3.8f %3.8f) \n with function\'s value %3.8f'% \
        (bestIndividual.position.xPosition, bestIndividual.position.yPosition, bestIndividual.fitness) )

    def multipleRuns(self):
        (mean, sd) = self.__controller.statisticsMultipleRun(self.__xMinimalValue, self.__xMaximalValue, self.__yMinimalValue, self.__yMaximalValue)
        print("The mean of all the results is " + str(mean) + ", and the standard deviation " + str(sd))

    def runForPlot(self):
        bestFitnessList = self.__controller.runForPlot(self.__xMinimalValue, self.__xMaximalValue, self.__yMinimalValue, self.__yMaximalValue)
        plt.plot(bestFitnessList)
        plt.show()