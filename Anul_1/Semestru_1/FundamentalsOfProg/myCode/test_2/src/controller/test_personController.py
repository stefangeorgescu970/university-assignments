"""
Created on 19/12/2016
@author Stefan
"""
from unittest import TestCase

from src.controller.PersonController import PersonController
from src.domain.entities import Person
from src.domain.validators import PersonValidator, RepositoryException
from src.repository.PersonRepository import PersonRepository


class TestPersonController(TestCase):
    def setUp(self):
        super().setUp()
        self.__person_validator = PersonValidator()
        self.__person_repository = PersonRepository(self.__person_validator)
        self.__person_controller = PersonController(self.__person_repository)

    def test_get_all(self):
        self.assertEqual(10, len(self.__person_controller.get_all()), "Get all not ok")

    def test_add_person(self):
        self.__person_controller.add_person(11)
        self.assertEqual(11, len(self.__person_controller.get_all()), "Add not ok")

    def test_get_number_ill_persons(self):
        self.assertEqual(2, self.__person_controller.get_number_ill_persons(), "ill not ok")

    def test_get_ill(self):
        person = Person(1, 'nonvaccinated', 'healthy')
        person.get_ill()
        self.assertEqual(False, person.is_healthy, "Getting ill not ok")

    def test_another_day_ill(self):
        person = Person(1, 'nonvaccinated', 'ill')
        self.__person_controller.another_day_ill(person)
        self.assertEqual(person.days_ill, 1, "Days ill not ok.")
        person.days_ill = 3
        self.__person_controller.another_day_ill(person)
        self.assertEqual(person.days_ill, 0, "days ill not ok")
        self.assertEqual(person.is_healthy, True, "Getting well not ok")

    def test_vaccinate(self):
        self.__person_controller.vaccinate(2)
        person = self.__person_repository.find_by_id(2)
        self.assertEqual(person.is_immune, True, "vaccinate not ok.")
        self.assertRaises(RepositoryException, self.__person_controller.vaccinate, 1)

    def test_simulate_new_day(self):
        self.__person_controller.simulate_new_day()
        self.assertEqual(4, self.__person_controller.get_number_ill_persons())



