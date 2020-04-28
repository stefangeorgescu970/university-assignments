"""

this is an example
further work is still necessary in order for this code to work!!!

"""

from math import *


def normaliseData(noExamples, noFeatures, trainData, noTestExamples, testData):
    # statistical normalisation
    for j in range(noFeatures):
        summ = 0.0
        for i in range(noExamples):
            summ += trainData[i][j]
        mean = summ / noExamples
        squareSum = 0.0
        for i in range(noExamples):
            squareSum += (trainData[i][j] - mean) ** 2
        deviation = sqrt(squareSum / noExamples)
        for i in range(noExamples):
            trainData[i][j] = (trainData[i][j] - mean) / deviation
        for i in range(noTestExamples):
            testData[i][j] = (testData[i][j] - mean) / deviation
    # min-max normalization
    """
    for j in range(noFeatures):
        minn=min([trainData[i][j] for i in range(noExamples)])
        maxx=max([trainData[i][j] for i in range(noExamples)])
        for i in range(noExamples):
            trainData[i][j]=LIM_MIN+trainData[i][j]*(LIM_MAX-LIM_MIN)/(maxx - minn)
         for i in range(noTestExamples):
            testData[i][j]=LIM_MIN+testData[i][j]*(LIM_MAX-LIM_MIN)/(maxx - minn)
    """
