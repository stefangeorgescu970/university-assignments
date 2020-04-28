"""
Created on 10/03/2018
@author Stefan
"""

import itertools
from math import sqrt


class Math:

    @staticmethod
    def checkEqual3(lst):
        return lst[1:] == lst[:-1]

    @staticmethod
    def getPermutations(numbersList):
        if not Math.checkEqual3(numbersList):
            return set(list(itertools.permutations(numbersList)))
        return numbersList

    @staticmethod
    def is_square(n):
        return sqrt(n).is_integer()

    @staticmethod
    def isqrt(x):
        if x < 0:
            raise ValueError('square root not defined for negative numbers')
        n = int(x)
        if n == 0:
            return 0
        a, b = divmod(n.bit_length(), 2)
        x = 2 ** (a+b)
        while True:
            y = (x + n//x)//2
            if y >= x:
                return x
            x = y




    @staticmethod
    def combinations(mySet, length):
        return list(itertools.combinations_with_replacement(mySet, length))

    @staticmethod
    def getRequiredPermutation(mySet, length):
        finalSet = []
        combinations = Math.combinations(mySet, length)
        for combo in combinations:
            permList = list(combo)
            perms = Math.getPermutations(permList)
            finalSet.append(perms)
        return finalSet
