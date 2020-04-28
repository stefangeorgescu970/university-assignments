"""
Created on 26/03/2018
@author Stefan
"""
import numpy

from Domain.Exception import AppException
from Domain.Individual import Individual
from Utils.AppConstants import AppConstants


class Algorithm:

    __iterationNumber = int
    __mutationProbability = None

    def __init__(self, problem, population):
        self.__problem = problem
        self.__population = population
        self.readParameters(AppConstants.ALGORITHM_PARAMETERS_FILE)
        self.generatePopulation()

    def readParameters(self, fileName):
        fileHandler = open(fileName, "r")
        fileContent = fileHandler.readlines()
        fileContent = [x.strip() for x in fileContent]
        for line in fileContent:
            line = line.split(":")
            if line[0].strip() == AppConstants.ITERATION_NUMBER:
                self.__iterationNumber = int(line[1].strip())
            elif line[0].strip() == AppConstants.POPULATION_SIZE:
                self.__population.setNumberOfIndividuals(int(line[1].strip()))
            elif line[0].strip() == AppConstants.MUTATION_PROBABILITY:
                self.__mutationProbability = float(line[1].strip())
            else:
                raise AppException("Faulty parameters file.")

    def iteration(self):
        (individual1, individual2) = self.__population.selection()
        if individual1 is not None:
            newIndividual = Individual.crossover(individual1, individual2)
            newIndividual.mutate(self.__mutationProbability, self.__problem)
            fitnessCrossover = newIndividual.fitness(self.__problem)
            if (individual1.getFitness() > individual2.getFitness()) and (individual1.getFitness() > fitnessCrossover):
                self.__population.replace(individual1, newIndividual)
            if (individual2.getFitness() > individual1.getFitness()) and (individual2.getFitness() > fitnessCrossover):
                self.__population.replace(individual2, newIndividual)

    def run(self):
        for index in range(self.__iterationNumber):
            self.iteration()
        return self.__population.evaluate(self.__problem)

    def statisticsMultipleRuns(self, numberOfRuns):
        self.resetPopulation()
        bestIndividuals = []
        for index in range(numberOfRuns):
            bestIndividuals.append(self.run())
            self.resetPopulation()
        fitnessValues = [individual.getFitness() for individual in bestIndividuals]
        return numpy.mean(fitnessValues), numpy.std(fitnessValues)

    def statisticsForPlot(self):
        self.resetPopulation()

        bestFitnessList = [min(individual.getFitness() for individual in self.__population.getIndividualsList())]
        for index in range(self.__iterationNumber):
            self.iteration()
            bestFitnessList.append(min(individual.getFitness() for individual in self.__population.getIndividualsList()))

        return bestFitnessList

    def generatePopulation(self):
        populationSize = self.__population.getNumberOfIndividuals()
        for index in range(populationSize):
            newIndividual = self.__problem.generateIndividual()
            newIndividual.fitness(self.__problem)
            self.__population.appendIndividual(newIndividual)

    def resetPopulation(self):
        self.__population.resetPopulation()
        self.generatePopulation()
