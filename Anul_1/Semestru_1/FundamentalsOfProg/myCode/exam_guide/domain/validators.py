"""
Created on 28/01/2017
@author Stefan
"""


class GradeValidator(object):
    @staticmethod
    def validate(grade):
        if grade.value < 0 or grade.value > 10:
            return False
        return True


class StudentValidator(object):
    @staticmethod
    def validate(student):
        if len(student.name) == 0 or len(student.group) == 0:
            return False
        return True
