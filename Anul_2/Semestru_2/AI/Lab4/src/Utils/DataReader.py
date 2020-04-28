"""
Created on 06/05/2018
@author Stefan
"""
import copy

from math import sqrt

from Utils.DataCluster import DataCluster

import xlrd

from Utils.DataRow import DataRow


class DataReader:
    def __init__(self):
        self.testData = DataCluster()
        self.learningData = DataCluster()
        self.fileName = "../Resources/CTG.xls"
        self.initialiseData()
        self.rawTestData = copy.deepcopy(self.testData)
        self.rawLearningData = copy.deepcopy(self.learningData)
        self.normaliseData()

    def initialiseData(self):
        numberOfLearningResult1 = 0
        numberOfLearningResult2 = 0
        numberOfLearningResult3 = 0
        workbook = xlrd.open_workbook(self.fileName)
        dataWorksheet = workbook.sheet_by_name("Data")
        for rowIndex in range(2, dataWorksheet._dimnrows - 3):
            measurements = []
            for columnIndex in range(10, 31):
                measurements.append(dataWorksheet.cell(rowIndex, columnIndex).value)

            expectedOutput = int(dataWorksheet.cell(rowIndex, 45).value)
            dataRow = DataRow(measurements, expectedOutput)

            if expectedOutput == 1 and numberOfLearningResult1 < 75:
                self.learningData.addDataRow(dataRow)
                numberOfLearningResult1 += 1
            elif expectedOutput == 2 and numberOfLearningResult2 < 75:
                self.learningData.addDataRow(dataRow)
                numberOfLearningResult2 += 1
            elif expectedOutput == 3 and numberOfLearningResult3 < 75:
                self.learningData.addDataRow(dataRow)
                numberOfLearningResult3 += 1
            else:
                self.testData.addDataRow(dataRow)

    def normaliseData(self):
        for feature in range(len(self.learningData.dataRows[0].measurements)):
            sum = 0.0
            for index in range(self.learningData.getNumberOfRows()):
                sum += self.learningData.dataRows[index][feature]
            mean = sum / self.learningData.getNumberOfRows()
            squareSum = 0.0
            for index in range(self.learningData.getNumberOfRows()):
                squareSum += (self.learningData.dataRows[index][feature] - mean) ** 2
            deviation = sqrt(squareSum / self.learningData.getNumberOfRows())
            if deviation != 0:
                for index in range(self.learningData.getNumberOfRows()):
                    self.learningData.dataRows[index][feature] = (self.learningData.dataRows[index][feature] - mean) / deviation
