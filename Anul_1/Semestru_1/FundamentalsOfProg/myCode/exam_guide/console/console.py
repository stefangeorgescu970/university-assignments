"""
Created on 28/01/2017
@author Stefan
"""
from domain.exceptions import ControllerException, RepositoryException


class Console(object):
    def __init__(self, student_controller, grade_controller, undo_controller):
        self.__student_controller = student_controller
        self.__grade_controller = grade_controller
        self.__undo_controller = undo_controller

    @staticmethod
    def __print_options():
        print("0. Exit app. \n"
              "1. Add a student. \n"
              "2. Remove a student. \n"
              "3. List all students. \n"
              "4. Assign a lab problem to a student. \n"
              "5. Assign a lab to a group. \n"
              "6. List all grades. \n"
              "7. Grade student. \n"
              "8. Rank all students in a group. \n"
              "9. Get list of all failing students. \n"
              "10.Undo. \n"
              "11.Redo")

    def add_student(self):
        new_id = input("Please enter student ID: ")
        new_id.strip()
        new_name = input("Please enter student name: ")
        new_name.strip()
        new_group = input("Please enter student group: ")
        new_group.strip()
        try:
            self.__student_controller.create(new_id, new_name, new_group)
            self.__undo_controller.register_operation('as', self.__student_controller.create, self.__student_controller.remove, int(new_id), new_name, new_group)
        except ControllerException as ce:
            print(ce)
        except RepositoryException as re:
            print(re)

    def remove_student(self):
        student_id = input("Please enter the ID of the student you want to delete: ")
        student_id.strip()
        try:
            student_id = int(student_id)
            if not self.__grade_controller.is_graded(student_id):
                deleted_student = self.__student_controller.remove(student_id)
                print("Student with id {0} was removed.".format(student_id))
                self.__undo_controller.register_operation('rs', self.__student_controller.remove, self.__student_controller.create, deleted_student.id, deleted_student.name, deleted_student.group)
        except ValueError:
            print("Given ID was not an integer.")
        except ControllerException as ce:
            print(ce)

    def list_students(self):
        student_list = self.__student_controller.get_all()
        if len(student_list) == 0:
            print("No students in the record.")
        else:
            for student in student_list:
                print(student)

    def assign_problem_stud(self):
        student_id = input("Please enter the ID of the student: ")
        student_id.strip()
        lab_no = input("Please enter the lab number: ")
        lab_no.strip()
        lab_problem_no = input("Please enter the problem number from that lab: ")
        lab_problem_no.strip()
        try:
            student_id = int(student_id)
            lab_no = int(lab_no)
            lab_problem_no = int(lab_problem_no)
            if self.__student_controller.find_by_id(student_id) is None:
                print("Student with ID {0} is not in the records.".format(student_id))
                return
            self.__grade_controller.assign_lab_to_student(student_id, lab_no, lab_problem_no)
            self.__undo_controller.register_operation('als', self.__grade_controller.assign_lab_to_student, self.__grade_controller.unassign_lab_from_student, student_id, lab_no, lab_problem_no)
        except ValueError:
            print("Not all input data was integer.")
        except ControllerException as ce:
            print(ce)

    def assign_lab_to_group(self):
        group = input("Please enter the number of the group: ")
        lab_no = input("PLease enter the number of the laboratory you wish to assign: ")
        lab_no.strip()
        group.strip()
        student_id_in_group = self.__student_controller.find_by_group(group)
        if student_id_in_group is None:
            print("There are no students in group number {0}.".format(group))
            return
        try:
            lab_no = int(lab_no)
            self.__grade_controller.assign_lab_to_group(student_id_in_group, lab_no)
            self.__undo_controller.register_operation('alg', self.__grade_controller.assign_lab_to_group, self.__grade_controller.unassign_lab_from_group, student_id_in_group, lab_no, group)
        except ValueError:
            print("Laboratory number is not an integer.")

    def list_grades(self):
        grade_list = self.__grade_controller.get_all()
        if len(grade_list) == 0:
            print("No grades in the record.")
        else:
            for grade in grade_list:
                print(grade)

    def grade_student(self):
        student_id = input("Enter the ID of the student you want to grade: ")
        student_id.strip()
        lab_no = input("Enter the number of the lab you want to grade student at: ")
        lab_no.strip()
        value = input("Enter the grade the student got: ")
        value.strip()
        try:
            student_id = int(student_id)
            lab_no = int(lab_no)
            value = int(value)
            if self.__student_controller.find_by_id(student_id) is None:
                print("Student with ID {0} is not in the records.".format(student_id))
                return
            self.__grade_controller.grade(student_id, lab_no, value)
            self.__undo_controller.register_operation('gs', self.__grade_controller.grade, self.__grade_controller.ungrade, student_id, lab_no, value)
        except ValueError:
            print("All arguments should have been integers.")
        except RepositoryException as re:
            print(re)
        except ControllerException as ce:
            print(ce)

    def group_ranking(self):
        group = input("Please enter the group you want the ranking for: ")
        group.strip()
        students_in_group = self.__student_controller.find_by_group_dto(group)
        if students_in_group is None:
            print("There are no students in group number {0}.".format(group))
            return
        try:
            average_grade_list = self.__grade_controller.get_student_ranking(students_in_group)
            for item in average_grade_list:
                print(item)
        except ControllerException as ce:
            print(ce)

    def failing_students(self):
        try:
            student_id_name_list = self.__student_controller.get_all_name_id_dto()
            failing_students_list = self.__grade_controller.get_failing_students(student_id_name_list)
            for item in failing_students_list:
                print(item)
        except ControllerException as ce:
            print(ce)

    def undo(self):
        self.__undo_controller.undo()

    def redo(self):
        self.__undo_controller.redo()

    def run(self):
        option_dict = {1: self.add_student, 2: self.remove_student, 3: self.list_students, 4: self.assign_problem_stud,
                       5: self.assign_lab_to_group, 6: self.list_grades, 7: self.grade_student, 8: self.group_ranking,
                       9: self.failing_students, 10: self.undo, 11: self.redo}
        while True:
            self.__print_options()
            command = input("Please enter the desired command: ")
            try:
                command = int(command)
                if command == 0:
                    break
                option_dict[command]()
            except ValueError:
                print("Command given was not a number.")
            except KeyError:
                print("Command not available")

