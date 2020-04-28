"""
Created on 28/01/2017
@author Stefan
"""
from domain.entities import Student
from domain.exceptions import RepositoryException


class StudentRepo(object):
    def __init__(self, student_validator):
        self.__student_validator = student_validator
        self.__file_name = "/Users/Stefan/PycharmProjects/exam_guide/students.txt"
        self.__student_list = []
        self.__init_from_file()

    def store(self, student):
        if self.__student_validator.validate(student):
            self.__student_list.append(student)
            self.__save_to_file()
        else:
            raise RepositoryException("A student must have both a group and a name.")

    def delete(self, student):
        self.__student_list.remove(student)
        self.__save_to_file()

    def get_all(self):
        return self.__student_list

    def find(self, student_id):
        pass

    def __init_from_file(self):
        file_handler = open(self.__file_name, 'r')
        input_data = file_handler.read()
        input_data = input_data.strip("\n")
        input_data = input_data.split('\n')
        for line in input_data:
            this_line = line.split(' ')
            student = Student(int(this_line[0]), this_line[1], this_line[2])
            self.store(student)
        file_handler.close()

    def __save_to_file(self):
        student_list = self.get_all()
        to_save = ""
        for student in student_list:
            to_save += str(student.id) + " " + student.name + " " + student.group + "\n"
        file_handler = open(self.__file_name, 'w')
        file_handler.write(to_save)
        file_handler.close()

