"""
Created on 31/05/2018
@author Stefan
"""
from Model.Enums.FunctionType import FunctionType
from Model.Enums.ParameterName import ParameterNameStubs
from Model.Enums.WashingCycleEnum import WashingCycleEnum
from Model.Utils.FileUtil import FileUtil
from Model.Utils.LFunctionData import LFunctionData
from Model.Utils.RFunctionData import RFunctionData
from Model.Utils.TriangularFunctionData import TriangularFunctionData


class WashingCycle:
    def __init__(self, fileName):
        self.__fuzzySets = {}
        self.__minimalValue = None
        self.__maximalValue = None
        self.__initialiseValues(FileUtil.getParamsDict(fileName))

    def __initialiseValues(self, paramsDict):
        self.__minimalValue = float(paramsDict[ParameterNameStubs.Min])
        self.__maximalValue = float(paramsDict[ParameterNameStubs.Max])
        for fuzzyFunction in WashingCycleEnum:
            if paramsDict[fuzzyFunction.name + ParameterNameStubs.Type] == FunctionType.L_Function:
                leftValue = float(paramsDict[fuzzyFunction.name + ParameterNameStubs.Left])
                tipValue = float(paramsDict[fuzzyFunction.name + ParameterNameStubs.Tip])
                self.__fuzzySets[fuzzyFunction.name] = LFunctionData(leftValue, tipValue)
            elif paramsDict[fuzzyFunction.name + ParameterNameStubs.Type] == FunctionType.R_Function:
                rightValue = float(paramsDict[fuzzyFunction.name + ParameterNameStubs.Right])
                tipValue = float(paramsDict[fuzzyFunction.name + ParameterNameStubs.Tip])
                self.__fuzzySets[fuzzyFunction.name] = RFunctionData(tipValue, rightValue)
            elif paramsDict[fuzzyFunction.name + ParameterNameStubs.Type] == FunctionType.TriangleFunction:
                leftValue = float(paramsDict[fuzzyFunction.name + ParameterNameStubs.Left])
                tipValue = float(paramsDict[fuzzyFunction.name + ParameterNameStubs.Tip])
                rightValue = float(paramsDict[fuzzyFunction.name + ParameterNameStubs.Right])
                self.__fuzzySets[fuzzyFunction.name] = TriangularFunctionData(leftValue, tipValue, rightValue)
            else:
                pass # TODO - raise some exception


    def computeValueFromMembershipDegree(self, membershipDegrees):
        #TODO - check if values are between 0 and 1, raise exception
        sum = 0
        divideBy = 0
        for fuzzyFunction in WashingCycleEnum:
            sum += self.__fuzzySets[fuzzyFunction.name].getTipValue() * membershipDegrees[fuzzyFunction]
            divideBy += membershipDegrees[fuzzyFunction]
        return sum / divideBy