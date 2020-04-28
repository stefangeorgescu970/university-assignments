"""
Created on 30/01/2017
@author Stefan
"""


class Sentence(object):
    def __init__(self, string):
        self.__string = string
        self.__hidden = []
        self.__hide_letters()

    def __hide_letters(self):
        """
        Function that updates the hidden list so we know whcih digits to hide and which not. Spaces will be considered
        hidden, but displaying will take care of that
        """
        for index in range(0, len(self.__string)):
            self.__hidden.append(True)
        for index, letter in enumerate(self.__string):
            if index == 0 or index == len(self.__string) - 1 or self.__string[index+1] == ' ' or self.__string[index -1] == ' ':
                self.__hidden[index] = False
                for index_2 in range(0, len(self.__string)-1):
                    if self.__string[index_2] == self.__string[index]:
                        self.__hidden[index_2] = False

    def __str__(self):
        """
        Override for the str func, so we can call print directly on the object
        :return: The string with the known characters shown, and the hidden ones with underscores
        """
        result = ""
        for index, letter in enumerate(self.__string):
            if letter == " ":
                result += letter
            elif self.__hidden[index]:
                result += "_"
            else:
                result += letter
        return result

    def find_letter(self, letter):
        """
        Searches for a letter in the sentence. If found, modifies it's status in the hidden list
        :param letter: the letter to seach for, single char
        :return: True if it was found, False otherwise
        """
        if letter in self.__string:
            for index, letter_ in enumerate(self.__string):
                if letter_ == letter:
                    self.__hidden[index] = False
            return True
        else:
            return False

    def did_win(self):
        """
        Function to check if the current state of the sentence object gives a winning scenario
        :return: True if the game finished, False otherwise
        """
        for index, letter in enumerate(self.__string):
            if letter != " " and self.__hidden[index] == True:
                return False
        return True

    @property
    def string(self):
        return self.__string

    @property
    def hidden(self):
        return self.__hidden
