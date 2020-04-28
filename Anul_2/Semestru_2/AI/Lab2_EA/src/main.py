"""
Created on 26/03/2018
@author Stefan
"""
from Domain.Algorithm import Algorithm
from Domain.Exception import AppException
from Domain.Population import Population
from Domain.Problem import Problem
from Utils.AppConstants import AppConstants
import matplotlib.pyplot as plt

if __name__ == '__main__':
    try:
        population = Population()
        problem = Problem()
        algorithm = Algorithm(problem, population)

        optimalIndividual = algorithm.run()
        print("Minimum of function is: " + str(optimalIndividual.getFitness()) + " for values: " + str(optimalIndividual.getXValue()) + ", " + str(optimalIndividual.getYValue()))

        # (mean, standardDeviation) = algorithm.statisticsMultipleRuns(AppConstants.NUMBER_OF_RUNS_FOR_STATISTICS)
        # print("The mean is: " + str(mean) + ", the standard deviation is: " + str(standardDeviation))
        #
        # bestFitnessList = algorithm.statisticsForPlot()
        #
        # plt.plot(bestFitnessList)
        # plt.show()

    except AppException as ae:
        print("An error occurred: " + ae.message)
