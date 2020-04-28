"""
Created on 31/05/2018
@author Stefan
"""
from Controller.Controller import Controller
from Model.Enums.ParameterName import ParameterNameInput
from Model.Utils.FileUtil import FileUtil


class Console:
    def __init__(self, inputFileName, outputFileName):
        self.__controller = Controller()
        self.__inputFile = inputFileName
        self.__outputFile = outputFileName
        self.__inputTexture = None
        self.__inputCapacity = None
        self.__readInputParameters()

    def __readInputParameters(self):
        paramDict = FileUtil.getParamsDict(self.__inputFile)
        self.__inputTexture = float(paramDict[ParameterNameInput.Texture])
        self.__inputCapacity = float(paramDict[ParameterNameInput.Capacity])

    def run(self):
        print("Read from file the following parameters")
        print("Texture: " + str(self.__inputTexture))
        print("Capacity: " + str(self.__inputCapacity))
        print("Computing cycle ...")
        exactNumber, cycle = self.__controller.computeCycle(self.__inputTexture, self.__inputCapacity)
        print("Computing done.")
        print("Suggested cycle is " + cycle.name)
        print("Additional float value obtained: " + str(exactNumber))
        FileUtil.dumpToFile(self.__outputFile, {"cycle":cycle.name, "value":str(exactNumber)})
        print("Wrote result to output file.")
        print("Terminating.")
