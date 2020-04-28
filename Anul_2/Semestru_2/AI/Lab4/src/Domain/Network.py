"""
Created on 06/05/2018
@author Stefan
"""
from math import exp

import numpy as np

from Domain.Layer import Layer


class Network:
    def __init__(self, numberOfInputs=0, numberOfOutputs=0, numberOfHiddenLayers=0, numberOfNeuronsPerHiddenLayer=0):
        self.LEARN_RATE = 0.01
        self.EPOCH_LIMIT = 1000
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.numberOfHiddenLayers = numberOfHiddenLayers
        self.numberOfNeuronsPerHiddenLayer = numberOfNeuronsPerHiddenLayer
        self.layers = [Layer(self.numberOfInputs, 0)]
        self.layers += [Layer(self.numberOfNeuronsPerHiddenLayer, self.numberOfInputs)]
        self.layers += [Layer(self.numberOfNeuronsPerHiddenLayer, self.numberOfNeuronsPerHiddenLayer) for k in
                        range(self.numberOfHiddenLayers - 1)]
        self.layers += [Layer(self.numberOfOutputs, self.numberOfNeuronsPerHiddenLayer)]

    def activate(self, inputs):
        # TODO - directly enumerate with index so we can get input beautifully - number of inputs = number of neurons in first layer
        index = 0
        for neuron in self.layers[0]:
            neuron.output = inputs[index]
            index += 1
        for layerIndex in range(1, self.numberOfHiddenLayers + 2):
            for neuron in self.layers[layerIndex]:
                info = []
                for index in range(neuron.numberOfInputs):
                    info.append(self.layers[layerIndex - 1].neurons[index].output)
                neuron.activate(info)

    def errorsBackPropagate(self, error):
        for layerIndex in range(self.numberOfHiddenLayers + 1, 1, -1):
            index = 0
            for neuron in self.layers[layerIndex]:
                if layerIndex == self.numberOfHiddenLayers + 1:
                    neuron.error = error
                else:
                    sumErrors = 0.0
                    for neuron2 in self.layers[layerIndex + 1]:
                        sumErrors += neuron2.weights[index] * neuron2.error
                    neuron.error = sumErrors
                for index2 in range(neuron.numberOfInputs):
                    netWeight = neuron.weights[index2] + self.LEARN_RATE * neuron.error * \
                                                         self.layers[layerIndex - 1].neurons[index2].output
                    neuron.weights[index2] = netWeight
                index += 1

    def errorComputationClassification(self, target, numberOfCategories):

        outputs = []

        for neuron in self.layers[self.numberOfHiddenLayers + 1]:
            outputs.append(neuron.output)

        # print(str(outputs))

        softmax = lambda x: np.exp(x) / np.sum(np.exp(x))
        transformedOutputs = softmax(outputs)

        maximum = transformedOutputs[0]
        computedLabel = 1
        for index in range(1, numberOfCategories):
            if transformedOutputs[index] > maximum:
                maximum = transformedOutputs[index]
                computedLabel = index + 1

        if target == computedLabel:
            error = 0
        else:
            error = 1

        return error

    @staticmethod
    def checkGlobalError(errors):
        correct = len(errors) - sum(errors)
        error = correct / len(errors)
        print("Percentage of errors: " + str(error))
        if error > 0.95:
            return True
        return False

    def learning(self, dataCluster):
        stopCondition = False
        epoch = 0
        while (not stopCondition) and (epoch < self.EPOCH_LIMIT):
            globalError = []
            for exampleNumber in range(dataCluster.getNumberOfRows()):
                self.activate(dataCluster.dataRows[exampleNumber].measurements)
                error = self.errorComputationClassification(dataCluster.dataRows[exampleNumber].expectedOutput, 3)
                globalError.append(error)
                self.errorsBackPropagate(error)
            stopCondition = self.checkGlobalError(globalError)
            epoch += 1

    def testing(self, dataCluster):
        globalError = []
        for exampleNumber in range(dataCluster.getNumberOfRows()):
            self.activate(dataCluster.dataRows[exampleNumber].measurements)
            globalError.append(self.errorComputationClassification(dataCluster.dataRows[exampleNumber].expectedOutput, 3))
