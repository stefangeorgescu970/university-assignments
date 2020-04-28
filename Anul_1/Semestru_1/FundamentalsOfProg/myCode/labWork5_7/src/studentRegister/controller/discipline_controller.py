from studentRegister.domain.entities import Discipline
from studentRegister.repository.repository import Repository


class DisciplineController(object):
    """
    A class for controlling the discipline repository
    """
    def __init__(self, discipline_repository):
        """
        Initializes with the repo
        :param student_repository: repo
        """
        self.__discipline_repository = discipline_repository

    def add_discipline(self, discipline_id, name):
        """
        Handles adding a discipline to the record
        :param discipline_id: int
        :param name: string
        Return the added discipline
        """
        discipline = Discipline(discipline_id, name)
        self.__discipline_repository.save(discipline)
        return discipline

    def delete_discipline(self, discipline_id):
        """
        Handles deleting a discipline from the record by its id.
        :param discipline_id: int
        Return the deleted discipline
        """
        return self.__discipline_repository.delete_by_id(discipline_id)

    def update_discipline(self, discipline_id, name):
        """
        Handles updating a discipline with a given id
        :param discipline_id: int
        :param name: new name, string
        Return the old discipline before updating together with the new one
        """
        discipline = Discipline(discipline_id, name)
        return discipline, self.__discipline_repository.update(discipline_id, discipline)

    def get_all(self):
        """
        Handles returning all the entities as a list.
        """
        return self.__discipline_repository.get_all()

    def find_by_id(self, discipline_id):
        """
        Handles searching if a discipline is in the record by its id.
        :param discipline_id: int
        :returns None if the entity is not found or the entity if it is found.
        """
        return self.__discipline_repository.find_by_id(discipline_id)

    def find_by_name(self, discipline_name):
        """
        Searches for a discipline by name or part of it's name.
        :param discipline_name: a string
        :return: a list with all the matches
        """
        return self.__discipline_repository.find_by_name(discipline_name)
    
    def init_discipline_data(self):
        if type(self.__discipline_repository) == Repository:
            self.__discipline_repository.save(Discipline(1, "Mathematical Analysis"))
            self.__discipline_repository.save(Discipline(2, "Fundamentals of Programming"))
            self.__discipline_repository.save(Discipline(3, "Algebra"))
            self.__discipline_repository.save(Discipline(4, "Computational Logic"))
        else:
            self.__discipline_repository.init_discipline_data()
