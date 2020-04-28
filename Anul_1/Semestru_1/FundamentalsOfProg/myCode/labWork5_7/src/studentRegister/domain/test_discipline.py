from unittest import TestCase
from studentRegister.domain.entities import Discipline


class TestDiscipline(TestCase):
    def setUp(self):
        super().setUp()
        self.__discipline = Discipline(1, "Math")

    def test_entity_id(self):
        self.assertEqual(self.__discipline.entity_id, 1, "ID not ok")

    def test_name(self):
        self.assertEqual(self.__discipline.name, "Math", "Name not ok")


