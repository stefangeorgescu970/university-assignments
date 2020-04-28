from unittest import TestCase

from studentRegister.domain.DTO import StudentDisciplineGradeDTO


class TestStudentDisciplineGradeDTO(TestCase):
    def setUp(self):
        super().setUp()
        self.__stud_disc_grade_dto = StudentDisciplineGradeDTO("Stefan", "Info", 10)

    def test_student_name(self):
        self.assertEqual(self.__stud_disc_grade_dto.student_name, "Stefan", "Stud not ok")

    def test_discipline_name(self):
        self.assertEqual(self.__stud_disc_grade_dto.discipline_name, "Info", "Disc not ok")

    def test_grade_value(self):
        self.assertEqual(self.__stud_disc_grade_dto.grade_value, 10, "Grade not ok")
