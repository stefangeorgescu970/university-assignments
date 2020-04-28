"""
Created on 06/05/2018
@author Stefan
"""


class DataCluster:
    def __init__(self):
        self.dataRows = []

    def addDataRow(self, dataRow):
        self.dataRows.append(dataRow)

    def getNumberOfRows(self):
        return len(self.dataRows)
