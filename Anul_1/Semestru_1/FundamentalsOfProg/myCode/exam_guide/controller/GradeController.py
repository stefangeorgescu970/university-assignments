"""
Created on 28/01/2017
@author Stefan
"""
import copy

from domain.dto import DTOAssembler
from domain.entities import Grade
from domain.exceptions import ControllerException


class GradeController(object):
    def __init__(self, grade_repo):
        self.__grade_repo = grade_repo

    def grade(self, student_id, lab_no, value):
        grades_obtained = self.find_by_student_id(student_id)
        can_be_graded = False
        old_grade = None
        for grade in grades_obtained:
            if grade.laboratory_no == lab_no:
                can_be_graded = True
                if grade.value != 0:
                    raise ControllerException("Student with ID {0} is already graded at laboratory number {1}.".format(student_id, lab_no))
                old_grade = grade
        if not can_be_graded:
            raise ControllerException("Student with ID {0} was not assigned a problem for laboratory number {1}.".format(student_id, lab_no))
        if can_be_graded:
            if old_grade is not None:
                self.__grade_repo.remove(old_grade)
            grade = Grade(student_id, lab_no, old_grade.laboratory_problem, value)
            self.__grade_repo.store(grade)

    def get_average_grade(self, student_id):
        grade_list = self.__grade_repo.get_all()
        no_grades = 0
        total_grade = 0
        for grade in grade_list:
            if grade.student_id == student_id and grade.value != 0:
                total_grade += grade.value
                no_grades += 1
        if total_grade != 0:
            return total_grade / no_grades
        return 0

    def get_student_ranking(self, student_dto_list):
        grade_list = self.__grade_repo.get_all()
        student_grades_list = []
        for student in student_dto_list:
            average_grade = self.get_average_grade(student.id)
            if average_grade != 0:
                student_grades_list.append(DTOAssembler.assemble_student_average_grade_dto(student.name, average_grade))
        if len(student_grades_list) == 0:
            raise ControllerException("No students graded in that group.")
        return sorted(student_grades_list, key=lambda student_dto: student_dto.average_grade, reverse=True)

    def get_failing_students(self, student_id_name_dto_list):
        failing_students_dto = []
        for student in student_id_name_dto_list:
            average_grade = self.get_average_grade(student.id)
            if average_grade > 0 and average_grade < 5:
                failing_students_dto.append(student)
        if len(failing_students_dto) == 0:
            raise ControllerException("No failing students, yet.")
        return failing_students_dto

    def get_all(self):
        return self.__grade_repo.get_all()

    def is_graded(self, student_id):
        grade_list = self.__grade_repo.get_all()
        for grade in grade_list:
            if grade.student_id == student_id and grade.value != 0:
                return True
        return False

    def find_by_student_id(self, student_id):
        grade_list = self.__grade_repo.get_all()
        grades_obtained = []
        for grade in grade_list:
            if grade.student_id == student_id:
                grades_obtained.append(grade)
        if len(grades_obtained) != 0:
            return grades_obtained
        return None

    def assign_lab_to_student(self, student_id, lab_no, lab_problem_no):
        grade_list = self.__grade_repo.get_all()
        for grade in grade_list:
            if grade.student_id == student_id and grade.laboratory_no == lab_no:
                raise ControllerException("Student with ID {0} has already been assigned a problem for lab no {1}.".format(student_id, lab_no))
        new_grade = Grade(student_id, lab_no, lab_problem_no, 0)
        self.__grade_repo.store(new_grade)

    def assign_lab_to_group(self, student_id_list, lab_no):
        current_problem = 1
        did_add = False
        for student_id in student_id_list:
            grades_obtained = self.find_by_student_id(student_id)
            is_assigned = False
            if grades_obtained is not None:
                for grade in grades_obtained:
                    if grade.laboratory_no == lab_no:
                        is_assigned = True
            if not is_assigned:
                new_grade = Grade(student_id, lab_no, current_problem, 0)
                self.__grade_repo.store(new_grade)
                print("Student with ID {0} was assigned problem number {1} at lab number {2}.".format(student_id, current_problem, lab_no))
                current_problem += 1
                did_add = True
        if not did_add:
            print("All students from that group were already assigned with a problem for lab number {0}.".format(lab_no))

    '''these don't actually work, you only need some setters and that's it'''

    def ungrade(self, student_id, lab_no):
        grade_list = self.__grade_repo.get_all()
        for grade in grade_list:
            if grade.student_id == student_id and grade.laboratory_no == lab_no:
                grade.__value = 0
        self.__grade_repo.__grade_list = copy.deepcopy(grade_list)

    def unassign_lab_from_group(self, student_id_in_group, lab_no, group):
        grade_list = self.__grade_repo.get_all()
        end_index = len(grade_list)
        index = 0
        while index < end_index:
            if grade_list[index].laboratory_no == lab_no and grade_list[index].student_id in student_id_in_group:
                grade_list.pop(index)
                end_index -= 1
            else:
                index += 1
        self.__grade_repo.__grade_list = copy.deepcopy(grade_list)

    def unassign_lab_from_student(self, student_id, lab_no):
        grade_list = self.__grade_repo.get_all()
        for index, grade in enumerate(grade_list):
            if grade.laboratory_no == lab_no and grade.student_id == student_id:
                delete_index = index
        self.__grade_repo.__grade_list.pop(index)

