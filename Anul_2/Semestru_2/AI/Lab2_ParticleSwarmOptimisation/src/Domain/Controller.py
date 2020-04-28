"""
Created on 08/04/2018
@author Stefan
"""
from random import random

import numpy

from Domain.Exception import AppException
from Domain.Swarm import Swarm
from Utils.AppConstants import AppConstants


class Controller:
    def __init__(self, xMinValue, xMaxValue, yMinValue, yMaxValue):
        self.__inertiaCoefficient = None
        self.__cognitiveLearningCoefficient = None
        self.__socialLearningCoefficient = None
        self.__iterationNumber = int
        self.__numberOfParticles = None
        self.readParameters(AppConstants.ALGORITHM_PARAMETERS_FILE)
        self.__swarm = Swarm(self.__numberOfParticles, xMinValue, xMaxValue, yMinValue, yMaxValue)

    def readParameters(self, fileName):
        fileHandler = open(fileName, "r")
        fileContent = fileHandler.readlines()
        fileContent = [x.strip() for x in fileContent]
        for line in fileContent:
            line = line.split(":")
            if line[0].strip() == AppConstants.ITERATION_NUMBER:
                self.__iterationNumber = int(line[1].strip())
            elif line[0].strip() == AppConstants.NUMBER_OF_PARTICLES:
                self.__numberOfParticles = int(line[1].strip())
            elif line[0].strip() == AppConstants.INERTIA_COEFFICIENT:
                self.__inertiaCoefficient = float(line[1].strip())
            elif line[0].strip() == AppConstants.COGNITIVE_LEARNING_COEFFICIENT:
                self.__cognitiveLearningCoefficient = float(line[1].strip())
            elif line[0].strip() == AppConstants.SOCIAL_LEARNING_COEFFICIENT:
                self.__socialLearningCoefficient = float(line[1].strip())
            else:
                raise AppException("Faulty parameters file.")

    def resetPopulation(self, xMinValue, xMaxValue, yMinValue, yMaxValue):
        self.__swarm = Swarm(self.__numberOfParticles, xMinValue, xMaxValue, yMinValue, yMaxValue)



    def iteration(self):
        for particle in self.__swarm.particles:
            bestNeighbour = Swarm.getBestNeighbour(particle)
            velocity = particle.velocity
            velocity.xChange = self.__inertiaCoefficient * velocity.xChange
            velocity.xChange = velocity.xChange + self.__socialLearningCoefficient * random() * (bestNeighbour.position.xPosition - particle.position.xPosition)
            velocity.xChange = velocity.xChange + self.__cognitiveLearningCoefficient * random() * (particle.bestPosition.xPosition - particle.position.xPosition)

            velocity.yChange = self.__inertiaCoefficient * velocity.yChange
            velocity.yChange = velocity.yChange + self.__socialLearningCoefficient * random() * (bestNeighbour.position.yPosition - particle.position.yPosition)
            velocity.yChange = velocity.yChange + self.__cognitiveLearningCoefficient * random() * (particle.bestPosition.yPosition - particle.position.yPosition)


        for particle in self.__swarm.particles:
            position = particle.position

            position.xPosition = position.xPosition + particle.velocity.xChange
            position.yPosition = position.yPosition + particle.velocity.yChange

            particle.position = position

    def runAlgorithm(self):
        for run in range(self.__iterationNumber):
            self.iteration()
        bestIndividual = min(self.__swarm.particles)
        return bestIndividual

    def statisticsMultipleRun(self, xMinValue, xMaxValue, yMinValue, yMaxValue):
        bestIndividuals = []
        for index in range(AppConstants.NUMBER_OF_RUNS_FOR_STATISTICS):
            self.resetPopulation(xMinValue, xMaxValue, yMinValue, yMaxValue)
            bestIndividuals.append(self.runAlgorithm())
        fitnessValues = [individual.fitness for individual in bestIndividuals]
        return numpy.mean(fitnessValues), numpy.std(fitnessValues)

    def runForPlot(self, xMinValue, xMaxValue, yMinValue, yMaxValue):
        self.resetPopulation(xMinValue, xMaxValue, yMinValue, yMaxValue)
        fitnessValues = []
        for run in range(self.__iterationNumber):
            self.iteration()
            fitnessValues.append(min(self.__swarm.particles).fitness)
        return fitnessValues
