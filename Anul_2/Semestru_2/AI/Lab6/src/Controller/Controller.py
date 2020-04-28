"""
Created on 31/05/2018
@author Stefan
"""
import operator

from Model.Capacity import Capacity
from Model.ClothesTexture import ClothesTexture
from Model.Enums.CapacitiesEnum import CapacitiesEnum
from Model.Enums.ClothesTexturesEnum import ClothesTexturesEnum
from Model.Enums.WashingCycleEnum import WashingCycleEnum
from Model.WashingCycle import WashingCycle

class Controller:
    def __init__(self):
        self.__textureFuzzy = ClothesTexture("/Users/Stefan/Documents/Facultate/codeOnly/Anul_2/Semestru_2/AI/Lab6/Resources/TextureData.in")
        self.__capacityFuzzy = Capacity("/Users/Stefan/Documents/Facultate/codeOnly/Anul_2/Semestru_2/AI/Lab6/Resources/CapacityData.in")
        self.__cycleFuzzy = WashingCycle("/Users/Stefan/Documents/Facultate/codeOnly/Anul_2/Semestru_2/AI/Lab6/Resources/CycleTypeData.in")
        self.__rules = [[WashingCycleEnum.Delicate, WashingCycleEnum.Easy, WashingCycleEnum.Normal],
                        [WashingCycleEnum.Easy, WashingCycleEnum.Normal, WashingCycleEnum.Normal],
                        [WashingCycleEnum.Easy, WashingCycleEnum.Normal, WashingCycleEnum.Intense],
                        [WashingCycleEnum.Easy, WashingCycleEnum.Normal, WashingCycleEnum.Intense]]


    def __evaluateInputData(self, texture, capacity):
        textureMembershipDegrees = self.__textureFuzzy.computeMembershipDegrees(texture)
        capacityMembershipDegrees = self.__capacityFuzzy.computeMembershipDegrees(capacity)
        return textureMembershipDegrees, capacityMembershipDegrees

    @staticmethod
    def computeMembershipMatrix(textureMD, capacityMD):
        matrix = []
        for texture in ClothesTexturesEnum:
            matrix.append([])
            for capacity in CapacitiesEnum:
                matrix[texture.value].append(min(capacityMD[capacity], textureMD[texture]))
        return matrix

    @staticmethod
    def getResultingCycle(cycleMembershipDegrees):
        return max(cycleMembershipDegrees.items(), key=operator.itemgetter(1))[0]

    def getCycleMembershipDegrees(self, membershipMatrix):
        dict = {}
        for fuzzy in WashingCycleEnum:
            dict[fuzzy] = 0
        for row in range(0, len(membershipMatrix)):
            for column in range(0, len(membershipMatrix[row])):
                if membershipMatrix[row][column] > dict[self.__rules[row][column]]:
                    dict[self.__rules[row][column]] = membershipMatrix[row][column]
        return dict

    def computeCycle(self, texture, capacity):
        textureMembDegrees, capacityMembDegrees = self.__evaluateInputData(texture, capacity)
        membershipMatrix = Controller.computeMembershipMatrix(textureMembDegrees, capacityMembDegrees)
        cycleMembershipDegrees = self.getCycleMembershipDegrees(membershipMatrix)
        answer = self.__cycleFuzzy.computeValueFromMembershipDegree(cycleMembershipDegrees)
        return answer, Controller.getResultingCycle(cycleMembershipDegrees)