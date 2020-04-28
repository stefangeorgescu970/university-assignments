"""
Created on 30/01/2017
@author Stefan
"""
import copy
import random

from domain.entities import Sentence
from domain.exceptions import ControllerException


class Controller(object):
    def __init__(self, repo):
        self.__repo = repo

    def add(self, new_sentence):
        """
        Adds e new sentence to the repo
        :param new_sentence: a string
        :return: Controller Exception if the sentence is already in the repo.
        """
        new_sentence = new_sentence.strip()
        sentence_list = self.__repo.get_all_string()
        if new_sentence in sentence_list:
            raise ControllerException("Sentence already exists.")
        sentence_to_add = Sentence(new_sentence)
        self.__repo.store(sentence_to_add)

    def get_random_sentence(self):
        """
        Gets a random sentence from the list
        :return: A Sentence object, deepcopied so changes will not affect the main list
        """
        sentence_list = self.__repo.get_all()
        sentence_number = random.randint(0, len(sentence_list) - 1)
        return copy.deepcopy(sentence_list[sentence_number])

    @staticmethod
    def get_available_letters(sentence):
        """
        Returns a list of the letters already known from a sentence
        :param sentence: a Sentence object
        :return: a list of chars
        """
        list = []
        for index, letter in enumerate(sentence.string):
            if letter != " " and sentence.hidden[index] == False and letter not in list:
                list.append(letter)
        return list
