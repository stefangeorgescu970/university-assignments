"""
Created on 06/05/2018
@author Stefan
"""


class DataRow:
    def __init__(self, measurements, expectedOutput):
        self.measurements = measurements
        self.expectedOutput = expectedOutput

    def __delitem__(self, key):
        self.measurements.__delattr__(key)

    def __getitem__(self, key):
        return self.measurements[key]

    def __setitem__(self, key, value):
        self.measurements[key] = value
