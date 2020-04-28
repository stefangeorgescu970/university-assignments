"""
Created on 28/01/2017
@author Stefan
"""
from domain.dto import DTOAssembler
from domain.entities import Student
from domain.exceptions import ControllerException


class StudentController(object):
    def __init__(self, student_repo):
        self.__student_repo = student_repo

    def create(self, id, name, group):
        try:
            id = int(id)
            new_student = Student(id, name, group)
            if self.find_by_id(id) is None:
                self.__student_repo.store(new_student)

            else:
                raise ControllerException("Duplicate ID {0}".format(id))
        except ValueError:
            raise ControllerException("ID given is not an integer.")

    def find_by_id(self, student_id):
        student_list = self.__student_repo.get_all()
        for student in student_list:
            if student_id == student.id:
                return student
        return None

    def remove(self, student_id):
        student_to_delete = self.find_by_id(student_id)
        if student_to_delete is None:
            raise ControllerException("Student is not in the records.")
        self.__student_repo.delete(student_to_delete)
        return student_to_delete

    def find_by_group(self, group):
        student_id_in_group = []
        student_list = self.__student_repo.get_all()
        for student in student_list:
            if student.group == group:
                student_id_in_group.append(student.id)
        if len(student_id_in_group) != 0:
            return student_id_in_group
        return None

    def find_by_group_dto(self, group):
        student_id_in_group = []
        student_list = self.__student_repo.get_all()
        for student in student_list:
            if student.group == group:
                student_id_in_group.append(DTOAssembler.assemble_student_id_name_dto(student.id, student.name))
        if len(student_id_in_group) != 0:
            return student_id_in_group
        return None

    def get_all(self):
        return self.__student_repo.get_all()

    def get_all_name_id_dto(self):
        student_list = self.__student_repo.get_all()
        student_id_name_dto_list = []
        for student in student_list:
            student_id_name_dto_list.append(DTOAssembler.assemble_student_id_name_dto(student.id, student.name))
        return student_id_name_dto_list
