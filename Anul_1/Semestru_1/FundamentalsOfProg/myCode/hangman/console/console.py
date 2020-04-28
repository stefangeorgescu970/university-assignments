"""
Created on 30/01/2017
@author Stefan
"""
from domain.exceptions import ControllerException, RepositoryException


class Console(object):
    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def __print_options():
        print("0. Exit program. \n"
              "1. Add new sentence. \n"
              "2. Start new game.")

    def add(self):
        """
        Function used to add a new sentence. Catches exceptions from lower layers.
        """
        new_string = input("Please enter the new sentence: ")
        try:
            self.__controller.add(new_string)
        except ControllerException as ce:
            print(ce)
        except RepositoryException as re:
            print(re)

    @staticmethod
    def get_hangman_letters(current_score):
        """
        Generates the hangman word corresponding to the current score of the player
        """
        return "hangman"[0:current_score]

    def start_game(self):
        """
        Main function for playing the game.
        :return:
        """
        sentence = self.__controller.get_random_sentence()
        current_score = 0
        try_list = self.__controller.get_available_letters(sentence)
        print("The sentence you have to solve is:")
        while current_score < 7:
            print(sentence)
            print("Current score: {0}".format(self.get_hangman_letters(current_score)))
            letter = input("Try for a letter: ")
            if letter == "exit":
                break
            elif len(letter) != 1:
                print("Only one letter at a time!")
            elif letter in try_list:
                print("You know about this letter!")
                current_score += 1
            else:
                try_list.append(letter)
                found = sentence.find_letter(letter)
                if not found:
                    current_score += 1
                else:
                    did_win = sentence.did_win()
                    if did_win:
                        print("You won!")
                        break
        if current_score == 7:
            print("Current score: hangman. \nYou lost.")

    def run(self):
        """
        Main running func
        """
        command_dict = {1: self.add, 2: self.start_game}
        while True:
            self.__print_options()
            command = input("Please choose next action: ")
            try:
                command = int(command)
                if command == 0:
                    break
                else:
                    command_dict[command]()
            except ValueError:
                print("Command value must be an int.")
            except KeyError:
                print("Command not available.")

        print("That's all folks!")
