"""
Created on 19/12/2016
@author Stefan
"""
from src.domain.entities import Person
from src.domain.validators import RepositoryException


class PersonRepository(object):
    def __init__(self, person_validator):
        self.__person_validator = person_validator
        self.__persons = {}
        self.__init_data()

    def save(self, person):
        if not self.__person_validator.validate(person):
            raise RepositoryException("invalid input data.")
        if not self.find_by_id(person.id) is None:
            raise RepositoryException("Duplicate ID {0}".format(person.id))
        self.__persons[person.id] = person

    def find_by_id(self, person_id):
        if person_id in self.__persons.keys():
            return self.__persons[person_id]
        return None

    def __init_data(self):
        input_file = open("andromeda_strain.txt", 'r')
        for person_data in input_file:
            person_data = person_data.strip('\n')
            person_data = person_data.split(",")
            person = Person(int(person_data[0]), person_data[1], person_data[2])
            self.save(person)

    def update(self, person):
        try:
            self.__persons[person.id] = person
        except KeyError:
            raise RepositoryException("Person with that ID does not exist.")

    def get_all(self):
        return list(self.__persons.values())
