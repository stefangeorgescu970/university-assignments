"""
Created on 06/05/2018
@author Stefan
"""
import copy

from math import sqrt
from random import random

from Utils.DataCluster import DataCluster

import xlrd

from Utils.DataRow import DataRow


class DataReader:
    def __init__(self):
        self.testData = DataCluster()
        self.learningData = DataCluster()
        self.fileName = "/Users/Stefan/Documents/Facultate/codeOnly/Anul_2/Semestru_2/AI/Lab5/resources/parkinsons_updrs.data.txt"
        self.initialiseData()

    def initialiseData(self):
        with open(self.fileName) as file:
            lines = [line.rstrip('\n') for line in file]
        content = [line.strip() for line in lines]
        content.pop(0) # Get rid of header in txt file

        for line in content:

            lineNumbers = line.split(",")

            expectedValue = float(lineNumbers[5])

            measurements = lineNumbers[6:22]

            measurements = [float(m) for m in measurements]

            newDataRow = DataRow(measurements, expectedValue)

            if random() < 0.1:
                self.learningData.addDataRow(newDataRow)
            else:
                self.testData.addDataRow(newDataRow)

    def __str__(self):
        str = "Learn Data \n"
        str += self.learningData.__str__()
        str += "\n"
        str += "Test Data \n"
        str += self.testData.__str__()
        return str


