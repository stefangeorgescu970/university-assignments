from unittest import TestCase

from studentRegister.domain.entities import Grade


class TestGrade(TestCase):
    def setUp(self):
        super().setUp()
        self.__grade = Grade(1, 2, 10)

    def test_entity_id(self):
        self.assertEqual(self.__grade.entity_id, "1.2", "ID not ok")

    def test_discipline_id(self):
        self.assertEqual(self.__grade.discipline_id, 1, "Discipline ID not ok")

    def test_student_id(self):
        self.assertEqual(self.__grade.student_id, 2, "Student ID not ok")

    def test_grade_value(self):
        self.assertEqual(self.__grade.grade_value, 10, "Grade not ok")


