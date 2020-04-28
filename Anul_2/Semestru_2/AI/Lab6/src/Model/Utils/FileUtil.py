"""
Created on 31/05/2018
@author Stefan
"""

class FileUtil:
    @staticmethod
    def getParamsDict(fileName):
        fileHandler = open(fileName, "r")
        fileContent = fileHandler.readlines()
        fileContent = [x.strip() for x in fileContent]
        paramsDict = {}
        for line in fileContent:
            line = line.split(":")
            paramsDict[line[0].strip()] = line[1].strip()
        fileHandler.close()
        return paramsDict

    @staticmethod
    def dumpToFile(fileName, outputDict):
        fileHandler = open(fileName, "w")
        for key, value in outputDict.items():
            fileHandler.write(key + ":" + value + "\n")
        fileHandler.close()