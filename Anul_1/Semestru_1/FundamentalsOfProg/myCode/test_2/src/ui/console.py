"""
Created on 19/12/2016
@author Stefan
"""
from src.domain.validators import RepositoryException

class Console(object):
    def __init__(self, person_controller):
        self.__person_controller = person_controller

    @staticmethod
    def __print_options():
        print("0. Exit the app. \n"
              "1. Add a person. \n"
              "2. List all persons. \n"
              "3. Simulate a new day. \n"
              "4. Vaccinate a person.")

    def add_person(self):
        person_id = input("Enter an id for the person: ")
        try:
            person_id = int(person_id)
            self.__person_controller.add_person(person_id)
        except RepositoryException as re:
            print(re)
        except ValueError:
            print("Id must be an int.")

    def list_all(self):
        persons = self.__person_controller.get_all()
        for person in persons:
            print(person)

    def simulate_new_day(self):
        self.__person_controller.simulate_new_day()

    def vaccinate(self):
        person_id = input("Enter the ID of the person you want to vaccinate: ")
        try:
            person_id = int(person_id)
            self.__person_controller.vaccinate(person_id)
        except RepositoryException as re:
            print(re)
        except ValueError:
            print("Id must be an int.")

    def run(self):
        commands = {1: self.add_person, 2: self.list_all, 3: self.simulate_new_day, 4: self.vaccinate}
        self.__print_options()
        while True:
            command = input("Enter a new command: ")
            command.strip()
            if command == '0':
                break
            try:
                commands[int(command)]()
            except ValueError:
                print("Command must be a number.")
            except KeyError:
                print("Unavailable command.")
