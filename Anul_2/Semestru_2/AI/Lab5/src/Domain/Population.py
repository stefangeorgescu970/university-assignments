"""
Created on 19/05/2018
@author Stefan
"""
import copy
from random import randint, random

from Domain.Chromosome import Chromosome


class Population:
    def __init__(self, learningData, testData, size):
        self.chromosomes = []
        self.learningData = learningData
        self.testData = testData

        for index in range(size):
            chromosome = Chromosome()
            chromosome.initialise()
            self.chromosomes.append(chromosome)

    @staticmethod
    def crossover(chromosome1, chromosome2):

        offspring1 = Chromosome()
        offspring2 = Chromosome()

        stop = True

        while stop:
            startChromosome1 = randint(0, chromosome1.size - 1)
            endChromosome1 = chromosome1.traverse(startChromosome1)
            startChromosome2 = randint(0, chromosome2.size - 1)
            endChromosome2 = chromosome2.traverse(startChromosome2)

            if len(offspring1.representation) > endChromosome1 + (endChromosome2 - startChromosome2 - 1) + (
                    chromosome1.size - endChromosome1 - 1) and \
                len(offspring2.representation) > endChromosome2 + (endChromosome1 - startChromosome1 - 1) + (
                    chromosome2.size - endChromosome2 - 1):
                stop = False

        # startChromosome1 = randint(0, chromosome1.size - 1)
        # endChromosome1 = chromosome1.traverse(startChromosome1)
        # startChromosome2 = randint(0, chromosome2.size - 1)
        # endChromosome2 = chromosome2.traverse(startChromosome2)

        # print("start1: " + str(startChromosome1))
        # print("end1: " + str(endChromosome1))
        # print("size1: " + str(chromosome1.size))
        # print("start2: " + str(startChromosome2))
        # print("end2: " + str(endChromosome2))
        # print("size2: " + str(chromosome2.size))
        #
        # print("off1 size: " + str(len(offspring1.representation)))
        # print("off2 size: " + str(len(offspring2.representation)))



        i = -1
        for i in range(startChromosome1):
            offspring1.representation[i] = chromosome1.representation[i]
            # print("current i value: " + str(i))
        for j in range(startChromosome2, endChromosome2):
            i += 1
            # print("current i value: " + str(i))
            offspring1.representation[i] = chromosome2.representation[j]
        for j in range(endChromosome1, chromosome1.size):
            i += 1
            # print("current i value: " + str(i))
            offspring1.representation[i] = chromosome1.representation[j]
        offspring1.size = i + 1

        i = -1
        for i in range(startChromosome2):
            # print("current i value: " + str(i))
            offspring2.representation[i] = chromosome2.representation[i]
        for j in range(startChromosome1, endChromosome1):
            i += 1
            # print("current i value: " + str(i))
            offspring2.representation[i] = chromosome1.representation[j]
        for j in range(endChromosome2, chromosome2.size):
            i += 1
            # print("current i value: " + str(i))
            offspring2.representation[i] = chromosome2.representation[j]
        offspring2.size = i + 1

        return [offspring1, offspring2]

    def computeFitnessOnPopulation(self):
        for chromosome in self.chromosomes:
            chromosome.computeFitness(self.learningData)

    def mutate(self, chance):
        for chromosome in self.chromosomes:
            if random() < chance:
                chromosome.mutate()

    def sort(self):
        self.chromosomes = sorted(self.chromosomes, key=lambda chromosome: chromosome.fitness)

    def generation(self):
        while True:

            self.computeFitnessOnPopulation()
            self.sort()

            print("Current best fitness: " + str(self.chromosomes[0].fitness))

            if self.chromosomes[0].fitness == 0:
                return

            children = Population.crossover(self.chromosomes[0], self.chromosomes[1])

            self.chromosomes[-2] = children[0]
            self.chromosomes[-1] = children[1]

            self.mutate(0.3)
