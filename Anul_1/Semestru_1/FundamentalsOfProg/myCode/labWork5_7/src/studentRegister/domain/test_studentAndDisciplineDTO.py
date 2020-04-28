from unittest import TestCase

from studentRegister.domain.DTO import StudentAndDisciplineDTO


class TestStudentAndDisciplineDTO(TestCase):
    def setUp(self):
        super().setUp()
        self.__stud__disc__dto = StudentAndDisciplineDTO("Mate", "Stefan")

    def test_discipline_name(self):
        self.assertEqual(self.__stud__disc__dto.discipline_name, "Mate", "Disc not ok")

    def test_student_name(self):
        self.assertEqual(self.__stud__disc__dto.student_name, "Stefan", "Stud not ok")

