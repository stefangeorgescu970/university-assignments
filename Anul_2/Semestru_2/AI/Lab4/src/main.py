"""
Created on 06/05/2018
@author Stefan
"""

from Domain.Network import Network
from Utils.DataReader import DataReader

if __name__ == '__main__':
    dr = DataReader()

    net = Network(21, 3, 2, 10)

    net.learning(dr.learningData)
    net.testing(dr.testData)
