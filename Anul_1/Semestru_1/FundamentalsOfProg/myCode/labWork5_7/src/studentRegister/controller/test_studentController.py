from unittest import TestCase

from studentRegister.controller.student_controller import StudentController
from studentRegister.domain.validators import StudentValidator
from studentRegister.repository.repository import Repository


class TestStudentController(TestCase):
    def setUp(self):
        super().setUp()
        student_repository = Repository(StudentValidator)
        self.__student_controller = StudentController(student_repository)

    def test_add_student(self):
        self.__student_controller.add_student(1, "Stefan")
        self.assertEqual(len(self.__student_controller.get_all()), 1, "Not ok")

    def test_delete_student(self):
        self.__student_controller.add_student(1, "Stefan")
        self.__student_controller.delete_student(1)
        self.assertEqual(len(self.__student_controller.get_all()), 0, "Not ok")

    def test_update_student(self):
        self.__student_controller.add_student(1, "Stefan")
        self.__student_controller.update_student(1, "Dragos")
        for item in self.__student_controller.get_all():
            self.assertEqual(item.name, "Dragos", "Not ok")

    def test_get_all(self):
        self.__student_controller.add_student(1, "Stefan")
        self.assertEqual(len(self.__student_controller.get_all()), 1, "Not ok")

    def test_find_by_id(self):
        self.__student_controller.add_student(1, "Stefan")
        self.assertEqual(self.__student_controller.find_by_id(2), None, "Not ok")

    def test_find_by_name(self):
        self.__student_controller.add_student(1, "Stefan")
        self.assertEqual(len(self.__student_controller.find_by_name("an")), 1, "Not ok")
        self.assertEqual(len(self.__student_controller.find_by_name("Cri")), 0, "Not ok")