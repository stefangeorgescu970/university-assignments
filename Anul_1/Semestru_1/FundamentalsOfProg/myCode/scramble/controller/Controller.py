"""
Created on 29/01/2017
@author Stefan
"""
import random


class Controller(object):
    def __init__(self, sentence_repo):
        self.__sentence_repo = sentence_repo

    def get_score(self):
        return self.__sentence_repo.get_score()

    def get_sentence(self):
        return self.__sentence_repo.get_sentence()

    def swap(self, word1, letter1, word2, letter2):
        self.__sentence_repo.swap(word1, letter1, word2, letter2)

    def scramble(self):
        current_sentence = self.__sentence_repo.get_sentence()
        current_score = current_sentence.score
        times_to_shuffle = random.randint(3, current_score - current_sentence.word_count * 2)
        for time in range(0, times_to_shuffle):
            try:
                word1 = random.randint(0, current_sentence.word_count-1)
                word2 = random.randint(0, current_sentence.word_count-1)
                letter1 = random.randint(1, len(current_sentence[word1])-2)
                letter2 = random.randint(1, len(current_sentence[word2])-2)
                self.__sentence_repo.swap(word1, letter1, word2, letter2)
            except ValueError:
                pass

    def did_win(self):
        if self.__sentence_repo.get_sentence() == self.__sentence_repo.get_initial_sentence():
            return True
        return False
