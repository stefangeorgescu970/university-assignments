from studentRegister.domain.DTO import NameAndGradeAssembler
from studentRegister.repository.MyCollection import MyCollection


class StatisticsController(object):
    """
    A class for computing all the data required for statistics
    """
    def __init__(self, student_repository, discipline_repository, link_repository, grade_repository):
        """
        Initializes the controller with all the repositories.
        :param student_repository: the student repo
        :param link_repository: the link repo
        :param grade_repository: the grade repo
        :param discipline_repository: the discipline repo
        """
        self.__student_repository = student_repository
        self.__link_repository = link_repository
        self.__grade_repository = grade_repository
        self.__discipline_repository = discipline_repository

    def get_all_enrolled(self, discipline_id):
        """
        Gets all the students enrolled at a given discipline.
        :param discipline_id: The discipline you want to get the students for.
        :return: a list with all the students
        """
        students = MyCollection()
        for item in self.__student_repository.get_all():
            newID = str(discipline_id) + "." + str(item.entity_id)
            if not self.__link_repository.find_by_id(newID) is None:
                students.append(item)
        return students

    def get_all_failing_students(self):
        """
        Gets all the students that are failing at one or more disciplines
        :return: The up mentioned list
        """
        students = MyCollection()
        for student in self.__student_repository.get_all():
            failing = False
            for grade in self.__grade_repository.get_all():
                if "." + str(student.entity_id) in grade.entity_id and grade.grade_value < 5:
                    failing = True
            if failing:
                students.append(student)
        return students

    def __create_student_and_grade_dto(self):
        students = self.__student_repository.get_all()
        dtos = MyCollection()
        for student in students:
            grades = self.__grade_repository.get_all_grades_by_student(student.entity_id)
            if sum(grades) != 0:
                averageGrade = sum(grades) / len(grades)
                name_and_grade_dto = NameAndGradeAssembler.create_name_and_grade_dto(student, averageGrade)
                dtos.append(name_and_grade_dto)
        return dtos

    def __create_discipline_and_grade_dto(self):
        disciplines = self.__discipline_repository.get_all()
        dtos = MyCollection()
        for discipline in disciplines:
            grades = self.__grade_repository.get_all_grades_by_discipline(discipline.entity_id)
            if sum(grades) != 0:
                averageGrade = sum(grades) / len(grades)
                name_and_grade_dto = NameAndGradeAssembler.create_name_and_grade_dto(discipline, averageGrade)
                dtos.append(name_and_grade_dto)
        return dtos

    @staticmethod
    def __compare_dtos_on_grade(dto1, dto2):
        if dto1.grade > dto2.grade:
            return -1
        if dto1.grade < dto2.grade:
            return 1
        return 0

    def get_sorted_students(self):
        """
        Gets a sorted list by average grade of all students.
        :return: The up mentioned list
        """
        results = self.__create_student_and_grade_dto()
        results.sort(self.__compare_dtos_on_grade)
        return results


    def get_sorted_disciplines(self):
        """
        Gets a sorted list by average grade of all disciplines, if there are grades for that discipline.
        :return: Imi plac cerealele
        """
        results = self.__create_discipline_and_grade_dto()
        results.sort(self.__compare_dtos_on_grade)
        return results
