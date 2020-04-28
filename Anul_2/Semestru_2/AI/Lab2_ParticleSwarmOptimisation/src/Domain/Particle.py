"""
Created on 08/04/2018
@author Stefan
"""
import copy
from math import sin
from numpy.random import random

from Domain.Coordinates import Coordinates
from Domain.Velocity import Velocity


class Particle:
    def __init__(self, xMinValue, xMaxValue, yMinValue, yMaxValue):

        self.__xMinValue = xMinValue
        self.__xMaxValue = xMaxValue
        self.__yMinValue = yMinValue
        self.__yMaxValue = yMaxValue

        xPosition = random() * (xMaxValue - xMinValue) + xMinValue
        yPosition = random() * (yMaxValue - yMinValue) + yMinValue

        self.__position = Coordinates(xPosition, yPosition)

        self.__fitness = self.computeFitness()

        self.__velocity = Velocity()

        self.__bestPosition=copy.deepcopy(self.__position)
        self.__bestFitness=self.__fitness

        self.__neighbours = []


    def computeFitness(self):

        x = self.__position.xPosition
        y = self.__position.yPosition

        return sin(x+y) + (x-y)**2 - 1.5*x + 2.5*y + 1

    @property
    def velocity(self):
        return self.__velocity

    @property
    def position(self):
        return self.__position

    @property
    def fitness(self):
        return self.__fitness

    @property
    def bestPosition(self):
        return self.__bestPosition

    @property
    def bestFitness(self):
        return self.__bestFitness

    @position.setter
    def position(self, newPosition):

        if newPosition.xPosition < self.__xMinValue:
            newPosition.xPosition = self.__xMinValue

        if newPosition.xPosition > self.__xMaxValue:
            newPosition.xPosition = self.__xMaxValue

        if newPosition.yPosition < self.__yMinValue:
            newPosition.yPosition = self.__yMinValue

        if newPosition.yPosition > self.__yMaxValue:
            newPosition.xPosition = self.__yMaxValue

        self.__position = copy.deepcopy(newPosition)
        # automatic evaluation of particle's fitness
        self.__fitness = self.computeFitness()
        # automatic update of particle's memory
        if self.__fitness < self.__bestFitness:
            self.__bestPosition = self.__position
            self.__bestFitness  = self.__fitness

    @property
    def neighbours(self):
        return self.__neighbours

    @neighbours.setter
    def neighbours(self, value):
        self.__neighbours = value

    def __lt__(self, other):
        return self.__fitness < other.fitness
