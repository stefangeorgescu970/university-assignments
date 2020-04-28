"""
Created on 28/01/2017
@author Stefan
"""
from domain.entities import Grade
from domain.exceptions import RepositoryException


class GradeRepo(object):
    def __init__(self, grade_validator):
        self.__grade_validator = grade_validator
        self.__file_name = "/Users/Stefan/PycharmProjects/exam_guide/grades.txt"
        self.__grade_list = []
        self.__init_from_file()

    def store(self, grade):
        if self.__grade_validator.validate(grade):
            self.__grade_list.append(grade)
            self.__save_to_file()
        else:
            raise RepositoryException("Grade value outside boundries.")

    def remove(self, grade):
        self.__grade_list.remove(grade)
        self.__save_to_file()

    def get_all(self):
        return self.__grade_list

    def __init_from_file(self):
        file_handler = open(self.__file_name, 'r')
        input_data = file_handler.read()
        input_data = input_data.strip("\n")
        input_data = input_data.split('\n')
        for line in input_data:
            this_line = line.split(' ')
            grade = Grade(int(this_line[0]), int(this_line[1]), int(this_line[2]), int(this_line[3]))
            self.store(grade)
        file_handler.close()

    def __save_to_file(self):
        grade_list = self.get_all()
        to_save = ""
        for grade in grade_list:
            to_save += str(grade.student_id) + " " + str(grade.laboratory_no) + " " + str(grade.laboratory_problem) + " " + str(grade.value) + '\n'
        file_handler = open(self.__file_name, 'w')
        file_handler.write(to_save)
        file_handler.close()