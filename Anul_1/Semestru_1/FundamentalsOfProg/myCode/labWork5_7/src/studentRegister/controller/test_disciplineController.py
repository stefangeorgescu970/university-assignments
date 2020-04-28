from unittest import TestCase

from studentRegister.controller.discipline_controller import DisciplineController
from studentRegister.domain.validators import DisciplineValidator
from studentRegister.repository.repository import Repository


class TestDisciplineController(TestCase):
    def setUp(self):
        super().setUp()
        discipline_repository = Repository(DisciplineValidator)
        self.__discipline_controller = DisciplineController(discipline_repository)

    def test_add_discipline(self):
        self.__discipline_controller.add_discipline(1, "Math")
        self.assertEqual(len(self.__discipline_controller.get_all()), 1, "Not ok")

    def test_delete_discipline(self):
        self.__discipline_controller.add_discipline(1, "Math")
        self.__discipline_controller.delete_discipline(1)
        self.assertEqual(len(self.__discipline_controller.get_all()), 0, "Not ok")

    def test_update_discipline(self):
        self.__discipline_controller.add_discipline(1, "Math")
        self.__discipline_controller.update_discipline(1, "ASC")
        for item in self.__discipline_controller.get_all():
            self.assertEqual(item.name, "ASC", "Not ok")

    def test_get_all(self):
        self.__discipline_controller.add_discipline(1, "Math")
        self.assertEqual(len(self.__discipline_controller.get_all()), 1, "Not ok")

    def test_find_by_id(self):
        self.__discipline_controller.add_discipline(1, "Math")
        self.assertEqual(self.__discipline_controller.find_by_id(2), None, "Not ok")

    def test_find_by_name(self):
        self.__discipline_controller.add_discipline(1, "Math")
        self.assertEqual(len(self.__discipline_controller.find_by_name("at")), 1, "Not ok")
        self.assertEqual(len(self.__discipline_controller.find_by_name("Romana")), 0, "Not ok")


