"""
Created on 08/04/2018
@author Stefan
"""
from random import randint

from Domain.Particle import Particle


class Swarm:
    def __init__(self, numberOfParticles, xMinValue, xMaxValue, yMinValue, yMaxValues):
        self.__sizeOfNeighbourhood = 20
        self.__numberOfParticles = numberOfParticles
        self.__particles = [Particle(xMinValue, xMaxValue, yMinValue, yMaxValues) for x in range(numberOfParticles)]
        self.selectNeighborhoods(self.__sizeOfNeighbourhood)

    def selectNeighborhoods(self, sizeOfNeighbourhood):

        if sizeOfNeighbourhood > len(self.__particles):
            sizeOfNeighbourhood = len(self.__particles) // 2

        for particle in self.__particles:
            neighbours = []
            for i in range(sizeOfNeighbourhood):
                x=randint(0, len(self.__particles)-1)
                while x in neighbours:
                    x=randint(0, len(self.__particles)-1)
                neighbours.append(x)
            neighbours = [self.__particles[index] for index in neighbours]
            particle.neighbours = neighbours

    @property
    def particles(self):
        return self.__particles

    @staticmethod
    def getBestNeighbour(particle):
        return min(particle.neighbours)


    def getBestParticles(self):
        pass

