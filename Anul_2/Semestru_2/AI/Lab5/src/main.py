"""
Created on 19/05/2018
@author Stefan
"""
from Domain.Population import Population
from Utils.DataReader import DataReader

if __name__ == '__main__':
    dataReader = DataReader()
    population = Population(dataReader.learningData, dataReader.testData, 50)
    population.generation()