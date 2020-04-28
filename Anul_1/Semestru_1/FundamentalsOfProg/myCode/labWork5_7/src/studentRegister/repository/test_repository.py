from unittest import TestCase

from studentRegister.domain.entities import Student, Grade
from studentRegister.domain.validators import StudentValidator, StudentValidatorException, GradeValidator
from studentRegister.repository.repository import Repository, RepositoryException


class TestRepository(TestCase):
    def setUp(self):
        super().setUp()
        self.__repository = Repository(StudentValidator)
        self.__grade_repo = Repository(GradeValidator)

    def test_save(self):
        student1 = Student(1, "Stefan")
        self.__repository.save(student1)
        self.assertEqual(len(self.__repository.get_all()), 1, "There should be one product in the repo")

        student2 = Student(1, "Dragos")
        self.assertRaises(RepositoryException, self.__repository.save, student2)

        student3 = Student("1", "Stefan")
        self.assertRaises(StudentValidatorException, self.__repository.save, student3)

    def test_find_by_id(self):
        student = Student(1, "Stefan")
        self.__repository.save(student)

        result = self.__repository.find_by_id(1)
        self.assertEqual(result, student, "Entities not equal")

        result = self.__repository.find_by_id(2)
        self.assertEqual(result, None, "Entities not equal")

    def test_update(self):
        student = Student(1, "Stefan")
        self.__repository.save(student)
        student_new = Student(1, "Adi")

        self.assertRaises(RepositoryException, self.__repository.update, 2, student_new)

        self.__repository.update(1, student_new)
        for item in self.__repository.get_all():
            self.assertEqual(student_new, item, "Error")

    def test_delete_by_id(self):
        student = Student(1, "Stefan")
        self.__repository.save(student)

        self.assertRaises(RepositoryException, self.__repository.delete_by_id, 2)
        self.__repository.delete_by_id(1)
        self.assertEqual(len(self.__repository.get_all()), 0, "Error at delete")
        self.assertRaises(RepositoryException, self.__repository.delete_by_id, 1)

    def test_find_by_name(self):
        student1 = Student(1, "Adrian")
        student2 = Student(2, "Stefan")
        self.__repository.save(student1)
        self.__repository.save(student2)

        self.assertEqual(len(self.__repository.find_by_name("an")), 2, "Not ok")
        self.assertEqual(len(self.__repository.find_by_name("Stefan")), 1, "Not ok")
        self.assertEqual(len(self.__repository.find_by_name("Cristian")), 0, "Not ok")

    def test_get_all_grades_by_discipline(self):
        grade1 = Grade(1, 1, 10)
        grade2 = Grade(1, 2, 10)
        grade3 = Grade(2, 1, 10)
        self.__grade_repo.save(grade1)
        self.__grade_repo.save(grade2)
        self.__grade_repo.save(grade3)

        self.assertEqual(len(self.__grade_repo.get_all_grades_by_discipline(1)), 2, "Not ok")
        self.assertEqual(len(self.__grade_repo.get_all_grades_by_discipline(2)), 1, "Not ok")


    def test_get_all_grades_by_student(self):
        grade1 = Grade(1, 1, 10)
        grade2 = Grade(1, 2, 10)
        grade3 = Grade(2, 1, 10)
        self.__grade_repo.save(grade1)
        self.__grade_repo.save(grade2)
        self.__grade_repo.save(grade3)

        self.assertEqual(len(self.__grade_repo.get_all_grades_by_student(1)), 2, "Not ok")
        self.assertEqual(len(self.__grade_repo.get_all_grades_by_student(2)), 1, "Not ok")
