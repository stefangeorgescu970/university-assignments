"""
Created on 26/03/2018
@author Stefan
"""
from random import randint, shuffle


class Population:
    def __init__(self):
        self.__numberOfIndividuals = int
        self.__individualsList = []

    def getIndividualsList(self):
        return self.__individualsList

    def evaluate(self, problem):
        return min(self.__individualsList)

    def selection(self):
        index1 = randint(0, len(self.__individualsList) - 1)
        index2 = randint(0, len(self.__individualsList) - 1)
        if index1 != index2:
            return self.__individualsList[index1], self.__individualsList[index2]
        else:
            return None, None

    def setNumberOfIndividuals(self, numberOfIndividuals):
        self.__numberOfIndividuals = numberOfIndividuals

    def getNumberOfIndividuals(self):
        return self.__numberOfIndividuals

    def appendIndividual(self, individual):
        self.__individualsList.append(individual)

    def replace(self, individualToReplace, newIndividual):
        self.__individualsList.remove(individualToReplace)
        self.__individualsList.append(newIndividual)
        shuffle(self.__individualsList)

    def resetPopulation(self):
        self.__individualsList.clear()
