"""
Created on 30/01/2017
@author Stefan
"""
from domain.entities import Sentence
from domain.exceptions import RepositoryException


class Repo(object):
    def __init__(self, validator, file_name):
        self.__validator = validator
        self.__sentence_list = []
        self.__file_name = file_name
        self.__init_from_file()

    def __init_from_file(self):
        """
        Function that reads from file and creates the corresponding sentences.
        """
        file_handler = open(self.__file_name, 'r')
        sentence_list = file_handler.read()
        sentence_list = sentence_list.split('\n')
        for sentence in sentence_list:
            sentence = sentence.strip()
            new_sentence = Sentence(sentence)
            self.store(new_sentence)
        file_handler.close()

    def __save_to_file(self):
        sentence_string = self.get_all_string()
        result = ""
        for sentence in sentence_string:
            result += sentence + "\n"
        result = result.strip("\n")
        file_handler = open(self.__file_name, 'w')
        file_handler.write(result)
        file_handler.close()

    def store(self, sentence):
        """
        Adds a new sentence to the repository
        :param sentence: a Sentence object
        :return: RepositoryException if the sentence does not respect the conditions.
        """
        if self.__validator.validate(sentence):
            self.__sentence_list.append(sentence)
            self.__save_to_file()
        else:
            raise RepositoryException("Sentence given does not respect the conditions.")

    def get_all_string(self):
        """
        Returns a list of all the sentences in the repo, in string from, all chars visible.
        """
        sentence_list = []
        for sentence in self.__sentence_list:
            sentence_list.append(sentence.string)
        return sentence_list

    def get_all(self):
        """
        Returns all the sentences in the repo as a list of objects
        """
        return self.__sentence_list

