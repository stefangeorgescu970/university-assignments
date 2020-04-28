"""
Created on 29/01/2017
@author Stefan
"""
from domain.Exceptions import UndoException


class Sentence(object):
    def __init__(self):
        self.__words = []
        self.__score = 0
        self.__word_count = 0

    def append(self, word):
        self.__words.append(word)
        self.__score += len(word)
        self.__word_count += 1

    @property
    def score(self):
        return self.__score

    @property
    def word_count(self):
        return self.__word_count

    def __setitem__(self, key, value):
        self.__words[key] = value

    def __getitem__(self, item):
        return self.__words[item]

    def __str__(self):
        final_string = ""
        for word in self.__words:
            final_string += str(word)
            final_string += " "
        return final_string.strip()

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)


class Word(object):
    def __init__(self, word_string):
        self.__letters = list(word_string)

    def __len__(self):
        return len(self.__letters)

    def __setitem__(self, key, value):
        self.__letters[key] = value

    def __getitem__(self, item):
        return self.__letters[item]

    def __str__(self):
        final_string = ""
        for letter in self.__letters:
            final_string += letter
        return final_string

class UndoObject(object):
    def __init__(self, word1, letter1, word2, letter2, swap_func):
        self.__word1 = word1
        self.__word2 = word2
        self.__letter1 = letter1
        self.__letter2 = letter2
        self.__swap_func = swap_func
        self.__did_undo = False

    def undo(self):
        if not self.__did_undo:
            self.__swap_func(self.__word1, self.__letter1, self.__word2, self.__letter2)
            self.__did_undo = True
        else:
            raise UndoException("You can only undo once.")
