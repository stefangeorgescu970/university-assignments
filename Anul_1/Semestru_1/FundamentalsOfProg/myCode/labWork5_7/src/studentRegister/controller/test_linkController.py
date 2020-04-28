from unittest import TestCase

from studentRegister.domain.entities import Student, Discipline
from studentRegister.domain.validators import LinkValidator, StudentValidator, DisciplineValidator
from studentRegister.repository.repository import Repository
from studentRegister.controller.link_controller import LinkController


class TestLinkController(TestCase):
    def setUp(self):
        super().setUp()
        self.__student_repository = Repository(StudentValidator)
        self.__discipline_repository = Repository(DisciplineValidator)
        self.__link_repository = Repository(LinkValidator)
        self.__link_controller = LinkController(self.__student_repository, self.__discipline_repository, self.__link_repository)

    def test_add_link(self):
        self.__link_controller.add_link(1,1)
        self.assertEqual(len(self.__link_controller.get_all()), 1, "Not ok")

    def test_get_all(self):
        self.__link_controller.add_link(1, 1)
        self.assertEqual(len(self.__link_controller.get_all()), 1, "Not ok")

    def test_find_by_id(self):
        self.__link_controller.add_link(1, 1)
        self.assertEqual(self.__link_controller.find_by_id("1.2"), None, "Not ok")

    def test_handle_delete_student(self):
        self.__link_controller.add_link(1, 1)
        self.__link_controller.handle_delete_student(1)
        self.assertEqual(len(self.__link_controller.get_all()), 0, "Not ok")

    def test_handle_delete_discipline(self):
        self.__link_controller.add_link(1, 1)
        self.__link_controller.handle_delete_discipline(1)
        self.assertEqual(len(self.__link_controller.get_all()), 0, "Not ok")

    def test_get_student_and_name_dtos(self):
        self.__link_controller.add_link(1, 1)
        self.__student_repository.save(Student(1, "Stefan"))
        self.__discipline_repository.save(Discipline(1, "Math"))
        dtos = self.__link_controller.get_student_and_name_dtos()
        self.assertEqual(len(dtos), 1, "Len not ok")
        self.assertEqual(dtos[0].student_name, "Stefan", "Stud not ok")
        self.assertEqual(dtos[0].discipline_name, "Math", "Disc not ok")
