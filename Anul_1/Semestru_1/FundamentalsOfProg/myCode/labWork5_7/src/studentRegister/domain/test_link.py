from unittest import TestCase

from studentRegister.domain.entities import Link


class TestLink(TestCase):
    def setUp(self):
        super().setUp()
        self.__link = Link(1, 2)

    def test_entity_id(self):
        self.assertEqual(self.__link.entity_id, "1.2", "Entity ID not ok")

    def test_discipline_id(self):
        self.assertEqual(self.__link.discipline_id, 1, "Disc id not ok")

    def test_student_id(self):
        self.assertEqual(self.__link.student_id, 2, "Stud ID not ok")

