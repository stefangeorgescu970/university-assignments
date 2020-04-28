"""
Created on 29/01/2017
@author Stefan
"""
import random

from domain.Exceptions import ConsoleException, UndoException
from domain.entities import UndoObject


class Console(object):
    def __init__(self, controller, undo_controller):
        self.__controller = controller
        self.__undo_controller = undo_controller

    def swap(self, *args):
        args = args[0]
        args = args.split('-')
        if len(args) != 2:
            raise ConsoleException("Argument list is invalid")
        for argument in args:
            argument = argument.strip()
            if len(argument) != 3:
                raise ConsoleException("Argument list is invalid")
        try:
            args[0] = args[0].strip().split(' ')
            args[1] = args[1].strip().split(' ')
            word1 = int(args[0][0])
            letter1 = int(args[0][1])
            word2 = int(args[1][0])
            letter2 = int(args[1][1])
            self.__controller.swap(word1, letter1, word2, letter2)
            last_operation = UndoObject(word1, letter1, word2, letter2, self.__controller.swap)
            self.__undo_controller.register_operation(last_operation)
        except ValueError:
            print("All indexes must be integers.")


    def undo(self):
        try:
            self.__undo_controller.undo()
        except UndoException as ue:
            print(ue)

    def run(self):
        self.__controller.scramble()
        current_score = self.__controller.get_score()
        while current_score > 0:
            print(self.__controller.get_sentence())
            print("Your current score is {0}.".format(current_score))
            command = input("Please enter your next command: ")
            command = command.split(' ', 1)
            if command[0] == 'swap':
                try:
                    self.swap(command[1])
                    current_score -= 1
                except IndexError:
                    print("The values you provided are not good.")
                except ConsoleException as ce:
                    print(ce)
            elif command[0] == 'undo':
                try:
                    self.undo()
                except UndoException as ue:
                    print(ue)
            elif command[0] == 'exit':
                break
            else:
                print("Command not available")
            if self.__controller.did_win():
                print("Congrats, you have won with score {0}.".format(current_score))
                break
        print("You lost.")

