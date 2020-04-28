"""
Created on 06/05/2018
@author Stefan
"""

from Domain.Neuron import Neuron


class Layer:
    def __init__(self, numberOfNeurons=0, numberOfInputs=0):
        self.iterator = 0
        self.numberOfNeurons = numberOfNeurons
        self.neurons = [Neuron(numberOfInputs) for k in range(self.numberOfNeurons)]

    def __iter__(self):
        return self

    def __next__(self):
        self.iterator += 1
        try:
            return self.neurons[self.iterator - 1]
        except IndexError:
            self.iterator = 0
            raise StopIteration
