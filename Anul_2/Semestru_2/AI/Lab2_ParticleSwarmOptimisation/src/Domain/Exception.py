"""
Created on 26/03/2018
@author Stefan
"""


class AppException (Exception):
    def __init__(self, message):
        self.message = message

