"""
Created on 28/01/2017
@author Stefan
"""


class DTOAssembler(object):
    @staticmethod
    def assemble_student_id_name_dto(student_id, name):
        return StudentIDGroupDTO(student_id, name)

    @staticmethod
    def assemble_student_average_grade_dto(name, average_grade):
        return StudentAverageGradeDTO(name, average_grade)


class StudentIDGroupDTO(object):
    def __init__(self, student_id, name):
        self.__id = student_id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return str(self.id) + ' ' + self.name


class StudentAverageGradeDTO(object):
    def __init__(self, name, average_grade):
        self.__name = name
        self.__average_grade = average_grade

    @property
    def name(self):
        return self.__name

    @property
    def average_grade(self):
        return self.__average_grade

    def __str__(self):
        return self.name + ' ' + str(self.average_grade)
