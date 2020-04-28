"""
Created on 19/12/2016
@author Stefan
"""
class AppException(Exception):
    pass


class RepositoryException(AppException):
    pass


class PersonValidator(object):

    def validate(self, person):
        return True
