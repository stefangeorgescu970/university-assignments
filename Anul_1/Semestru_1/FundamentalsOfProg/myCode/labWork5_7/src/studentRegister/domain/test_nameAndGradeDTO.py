from unittest import TestCase

from studentRegister.domain.DTO import NameAndGradeDTO


class TestNameAndGradeDTO(TestCase):
    def setUp(self):
        super().setUp()
        self.__name_and_grade = NameAndGradeDTO("Adrian", 10)

    def test_name(self):
        self.assertEqual(self.__name_and_grade.name, "Adrian", "Name not ok")

    def test_grade(self):
        self.assertEqual(self.__name_and_grade.grade, 10, "Grade not ok")

