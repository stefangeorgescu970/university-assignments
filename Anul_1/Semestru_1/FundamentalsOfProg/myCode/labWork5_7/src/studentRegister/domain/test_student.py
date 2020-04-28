from unittest import TestCase
from studentRegister.domain.entities import Student


class TestStudent(TestCase):
    def setUp(self):
        super().setUp()
        self.__student = Student(1, "Stefan")

    def test_entity_id(self):
        self.assertEqual(self.__student.entity_id, 1, "StudentID not equal")

    def test_name(self):
        self.assertEqual(self.__student.name, "Stefan", "Name not ok")
