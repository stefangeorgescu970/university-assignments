"""
Created on 05/05/2018
@author Stefan
"""
from random import random


class Neuron:
    def __init__(self, numberOfInputs=0):
        self.numberOfInputs = numberOfInputs
        self.weights = [(random() * 2 - 1) for k in range(self.numberOfInputs)]          # MIN_W = -1, MAX_W = 1
        self.output = 0
        self.error = 0

    def activate(self, info):
        if self.numberOfInputs == 0:
            self.output = info
        else:
            net = 0.0
            for i in range(self.numberOfInputs):
                net += info[i] * self.weights[i]
            self.output = net

