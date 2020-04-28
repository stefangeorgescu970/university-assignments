"""
Created on 30/01/2017
@author Stefan
"""


class GeneralException(Exception):
    """
    General exception from which all exceptions inherit
    """
    pass


class RepositoryException(GeneralException):
    """
    Exception to be thrown in the repo
    """
    pass


class ControllerException(GeneralException):
    """
    Exception to be thrown in the controller
    """
    pass
