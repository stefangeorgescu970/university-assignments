"""
Created on 26/03/2018
@author Stefan
"""
from random import random


class Individual:

    __fitness = float

    def __init__(self, xValue, yValue):
        self.__xValue = xValue
        self.__yValue = yValue

    def getXValue(self):
        return self.__xValue

    def getYValue(self):
        return self.__yValue

    def getFitness(self):
        return self.__fitness

    def mutate(self, probability, problem):
        if probability > random():
            newIndividual = problem.generateIndividual()
            self.__xValue = newIndividual.getXValue()
            self.__yValue = newIndividual.getYValue()

    def fitness(self, problem):
        fitnessValue = problem.computeFunctionValue(self.__xValue, self.__yValue)
        self.__fitness = fitnessValue
        return fitnessValue

    @staticmethod
    def crossover(individual1, individual2):
        probability = random()
        xValue = probability * (individual1.getXValue() - individual2.getXValue()) + individual2.getXValue()
        yValue = probability * (individual1.getYValue() - individual2.getYValue()) + individual2.getYValue()
        return Individual(xValue, yValue)

    def __lt__(self, other):
        return self.__fitness < other.getFitness()
