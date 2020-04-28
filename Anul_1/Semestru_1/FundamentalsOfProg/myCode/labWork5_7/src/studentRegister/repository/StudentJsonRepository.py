"""
Created on 07/12/2016
@author Stefan
"""
import json

from studentRegister.domain.entities import Student
from studentRegister.repository.repository import Repository


class StudentJsonRepository(Repository):
    def __init__(self, student_validator, file_name):
        Repository.__init__(self, student_validator)
        self.__file_name = file_name

    @property
    def file_name(self):
        return self.__file_name

    def init_student_data(self):
        file = open(self.file_name)
        info = json.load(file)
        for key in info.keys():
            self.save(Student(int(key), info[key]))
        file.close()

    def __save_to_file(self):
        file = open(self.file_name, 'w')
        students = self.get_all()
        student_dict = {}
        for student in students:
            student_dict[student.entity_id] = student.name
        json.dump(student_dict, file)
        file.close()

    def save(self, entity):
        super().save(entity)
        self.__save_to_file()

    def update(self, entity_id, entity):
        super().update(entity_id, entity)
        self.__save_to_file()

    def delete_by_id(self, entity_id):
        super().delete_by_id(entity_id)
        self.__save_to_file()

