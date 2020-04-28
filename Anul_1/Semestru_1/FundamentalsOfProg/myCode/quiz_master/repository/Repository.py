"""
Created on 29/01/2017
@author Stefan
"""
from domain.entities import Question


class Repository(object):
    def __init__(self):
        self.__question_list = []
        self.__init_from_file()

    def store(self, qustion):
        self.__question_list.append(qustion)

    def get_all(self):
        return self.__question_list

    def __init_from_file(self):
        file_handler = open("/Users/Stefan/PycharmProjects/quiz_master/question_list.txt", 'r')
        init_data = file_handler.read()
        init_data = init_data.split('\n')
        for line in init_data:
            line = line.split(";")
            new_question = Question(int(line[0]), line[1], line[2], line[3], line[4], line[5], line[6])
            self.store(new_question)
        file_handler.close()