from studentRegister.domain.entities import Student
from studentRegister.repository.repository import Repository


class StudentController(object):
    """
    A class for controlling the student repository
    """
    def __init__(self, student_repository):
        """
        Initializes with the repo
        :param student_repository: repo
        """
        self.__student_repository = student_repository

    def add_student(self, student_id, name):
        """
        Handles adding a discipline to the record
        :param student_id: int
        :param name: string
        Returns the new student
        """
        student = Student(student_id, name)
        self.__student_repository.save(student)
        return student

    def delete_student(self, student_id):
        """
        Handles deleting a student from the record by its id.
        :param student_id: int
        Returns the deleted student
        """
        return self.__student_repository.delete_by_id(student_id)

    def update_student(self, student_id, name):
        """
        Handles updating a student with a given id
        :param student_id: int
        :param name: new name, string
        Returns the old student
        """
        student = Student(student_id, name)
        return student, self.__student_repository.update(student_id, student)

    def get_all(self):
        """
        Handles returning all the entities as a list.
        """
        return self.__student_repository.get_all()

    def find_by_id(self, student_id):
        """
        Handles searching if a student is in the record by his id.
        :param student_id: int
        :returns None if the entity is not found or the entity if it is found.
        """
        return self.__student_repository.find_by_id(student_id)

    def find_by_name(self, student_name):
        """
        Handles finding a student by a part of it's name
        :param student_name: a string containing the student's name
        :return: a list containing all matches
        """
        return self.__student_repository.find_by_name(student_name)
    
    def init_student_data(self):
        if type(self.__student_repository) == Repository:
            self.__student_repository.save(Student(1, "Adi Moldovan"))
            self.__student_repository.save(Student(2, "Cristi Nacu"))
            self.__student_repository.save(Student(3, "Stefan Georgescu"))
            self.__student_repository.save(Student(4, "Alexandra Dragodan"))
            self.__student_repository.save(Student(5, "Andrada Gae"))
            self.__student_repository.save(Student(6, "Monica Grigorovici"))
            self.__student_repository.save(Student(7, "Octavian Doica"))
            self.__student_repository.save(Student(8, "Ionut Grad"))
            self.__student_repository.save(Student(9, "Razvan Farte"))
            self.__student_repository.save(Student(10, "Laurentiu Duma"))
            self.__student_repository.save(Student(11, "Diana Dragos"))

        else:
            self.__student_repository.init_student_data()
