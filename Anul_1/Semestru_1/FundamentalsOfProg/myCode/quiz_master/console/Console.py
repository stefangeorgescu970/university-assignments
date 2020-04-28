"""
Created on 29/01/2017
@author Stefan
"""
from domain.Exceptions import ConsoleException, ControllerException


class Console(object):
    def __init__(self, controller):
        self.__controller = controller

    def print_questions(self):
        question_list = self.__controller.get_all()
        for question in question_list:
            print(question)

    def add_question(self, *args):
        args = args[0].strip()
        args = args.split(";")
        if len(args) != 7:
            raise ConsoleException("Argument list is invalid.")
        self.__controller.add_question(args[0].strip(), args[1].strip(), args[2].strip(), args[3].strip(), args[4].strip(), args[5].strip(), args[6].strip())

    def create_quiz(self, *args):
        args = args[0].strip()
        args = args.split(' ')
        if len(args) != 3:
            raise ConsoleException("Argument list is invalid.")
        self.__controller.create_quiz(args[0].strip(), args[1].strip(), args[2].strip())

    def play_quiz(self, *args):
        args = args[0].strip()
        if "." not in args:
            raise ConsoleException("Argument list is invalid.")
        self.__controller.play_quiz(args)

    def run(self):
        while True:
            command = input("Enter the next command: ")
            command = command.split(' ', 1)
            if command[0] == 'list':
                self.print_questions()
            elif command[0] == 'exit':
                break
            elif command[0] == 'add':
                try:
                    self.add_question(command[1])
                except ConsoleException as ce:
                    print(ce)
                except ControllerException as ce:
                    print(ce)
                except IndexError:
                    print("Argument list is invalid.")
            elif command[0] == 'create':
                try:
                    self.create_quiz(command[1])
                except ControllerException as ce:
                    print(ce)
                except ConsoleException as ce:
                    print(ce)
                except IndexError:
                    print("Argument list is invalid.")
            elif command[0] == 'start':
                try:
                    self.play_quiz(command[1])
                except ConsoleException as ce:
                    print(ce)
                except IndexError:
                    print("Argument list is invalid.")
            else:
                print("Command not available.")
