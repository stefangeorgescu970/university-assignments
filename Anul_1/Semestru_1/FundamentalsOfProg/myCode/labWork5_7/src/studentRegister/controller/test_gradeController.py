from unittest import TestCase
from studentRegister.controller.grade_controller import GradeController
from studentRegister.domain.entities import Student, Discipline
from studentRegister.repository.repository import Repository
from studentRegister.domain.validators import GradeValidator, StudentValidator, DisciplineValidator


class TestGradeController(TestCase):
    def setUp(self):
        super().setUp()
        self.__student_repository = Repository(StudentValidator)
        self.__discipline_repository = Repository(DisciplineValidator)
        self.__grade_repository = Repository(GradeValidator)
        self.__grade_controller = GradeController(self.__student_repository, self.__discipline_repository, self.__grade_repository)

    def test_add_grade(self):
        self.__grade_controller.add_grade(1, 1, 10)
        self.assertEqual(len(self.__grade_controller.get_all()), 1, "Not ok")

    def test_get_all(self):
        self.__grade_controller.add_grade(1, 1, 10)
        self.assertEqual(len(self.__grade_controller.get_all()), 1, "Not ok")

    def test_find_by_id(self):
        self.__grade_controller.add_grade(1, 1, 10)
        self.assertEqual(self.__grade_controller.find_by_id("1.2"), None, "Not ok")

    def test_handle_delete_student(self):
        self.__grade_controller.add_grade(1, 1, 10)
        self.__grade_controller.handle_delete_student(1)
        self.assertEqual(len(self.__grade_controller.get_all()), 0, "Not ok")

    def test_handle_delete_discipline(self):
        self.__grade_controller.add_grade(1, 1, 10)
        self.__grade_controller.handle_delete_discipline(1)
        self.assertEqual(len(self.__grade_controller.get_all()), 0, "Not ok")

    def test_get_student_discipline_grade_dtos(self):
        self.__grade_controller.add_grade(1, 1, 10)
        self.__student_repository.save(Student(1, "Stefan"))
        self.__discipline_repository.save(Discipline(1, "Math"))
        dtos = self.__grade_controller.get_student_discipline_grade_dtos()
        self.assertEqual(len(dtos), 1, "Len not ok")
        self.assertEqual(dtos[0].student_name, "Stefan", "Stud not ok")
        self.assertEqual(dtos[0].discipline_name, "Math", "Disc not ok")
        self.assertEqual(dtos[0].grade_value, 10, "Grade not ok")
