"""
Created on 19/12/2016
@author Stefan
"""
from src.domain.entities import Person
from src.domain.validators import RepositoryException


class PersonController(object):
    def __init__(self, person_repository):
        self.__person_repository = person_repository

    def get_all(self):
        """
        Returns all the entities in the list
        """
        return self.__person_repository.get_all()

    def add_person(self, person_id):
        """
        Adds a person to the register
        """
        person = Person(person_id, 'nonvaccinated', 'healthy')
        self.__person_repository.save(person)

    def get_number_ill_persons(self):
        persons = self.get_all()
        result = 0
        for person in persons:
            if not person.is_healthy:
                result += 1
        return result

    def get_ill(self, person):
        person.get_ill()
        self.__person_repository.update(person)

    def another_day_ill(self, person):
        if person.days_ill == 3:
            person.days_ill = 0
            person.get_well()
        else:
            person.days_ill += 1
        self.__person_repository.update(person)

    def simulate_new_day(self):
        number_ill_persons = self.get_number_ill_persons()
        persons = self.get_all()
        for person in persons:
            if not person.is_healthy:
                self.another_day_ill(person)
            elif person.is_healthy and not person.is_immune and number_ill_persons > 0:
                self.get_ill(person)
                number_ill_persons -= 1

    def vaccinate(self, person_id):
        if self.__person_repository.find_by_id(person_id) is None:
            raise RepositoryException("Person does not exist.")
        person = self.__person_repository.find_by_id(person_id)
        if not person.is_healthy:
            raise RepositoryException("Person is not healthy.")
        person.vaccinate()
        self.__person_repository.update(person)
