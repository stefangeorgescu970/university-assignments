"""
Created on 28/01/2017
@author Stefan
"""


class GeneralException(Exception):
    pass


class RepositoryException(GeneralException):
    pass


class ControllerException(GeneralException):
    pass


class ConsoleException(GeneralException):
    pass