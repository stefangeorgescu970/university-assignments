"""
Created on 29/01/2017
@author Stefan
"""
import copy
import random

from domain.entities import Sentence, Word


class SentenceRepository(object):
    def __init__(self):
        self.__sentence = None
        self.__initial_sentence = None
        self.__file_name = "/Users/Stefan/PycharmProjects/scramble/sentences.txt"
        self.__init_from_file()

    def __init_from_file(self):
        file_handler = open(self.__file_name, 'r')
        input = file_handler.read()
        input = input.strip('\n')
        input = input.split('\n')
        selected_sentece = random.randint(0, len(input)-1)
        selected_sentece = input[selected_sentece]
        selected_sentece = selected_sentece.split(' ')
        final_sentence = Sentence()
        for word in selected_sentece:
            new_word = Word(word)
            final_sentence.append(new_word)
        self.__sentence = final_sentence
        self.__initial_sentence = copy.deepcopy(final_sentence)

    def get_score(self):
        return self.__sentence.score

    def get_sentence(self):
        return self.__sentence

    def get_initial_sentence(self):
        return self.__initial_sentence
    
    def swap(self, word1, letter1, word2, letter2):
        self.__sentence[word1][letter1], self.__sentence[word2][letter2] = self.__sentence[word2][letter2], self.__sentence[word1][letter1]

