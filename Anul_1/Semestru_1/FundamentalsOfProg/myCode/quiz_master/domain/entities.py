"""
Created on 29/01/2017
@author Stefan
"""


class Question(object):
    def __init__(self, question_id, text, answer1, answer2, answer3, correct_answer, difficulty):
        self.__question_id = question_id
        self.__text = text
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__correct_answer = correct_answer
        self.__difficulty = difficulty

    @property
    def question_id(self):
        return self.__question_id

    @property
    def text(self):
        return self.__text

    @property
    def difficulty(self):
        return self.__difficulty

    @property
    def correct_answer(self):
        return self.__correct_answer

    @property
    def answer1(self):
        return self.__answer1

    @property
    def answer2(self):
        return self.__answer2

    @property
    def answer3(self):
        return self.__answer3

    def __str__(self):
        return self.__text + "\n" + self.__answer1 + "\n" + self.__answer2 + "\n" + self.__answer3


class Quiz(object):
    def __init__(self, difficulty, no_of_questions, file_name):
        self.__question_list = []
        self.__difficulty = difficulty
        self.__main_directory = "/Users/Stefan/PycharmProjects/quiz_master/"
        self.__file_name = file_name
        self.__file_location = self.__main_directory + self.__file_name
        self.__no_of_questions = no_of_questions

    @property
    def difficulty(self):
        return self.__difficulty

    @property
    def no_of_questions(self):
        return self.__no_of_questions

    def get_questions(self):
        return self.__question_list

    def add_question(self, question):
        self.__question_list.append(question)

    def __len__(self):
        return len(self.__question_list)

    def store(self):
        file_handler = open(self.__file_location, 'w+')
        final_string = ""
        for question in self.__question_list:
            final_string += str(question.question_id) + ";" + question.text + ";" + question.answer1 + ";" + question.answer2 + ";" + question.answer3 + ";" + question.correct_answer + ";" + question.difficulty + "\n"
        file_handler.write(final_string)
        file_handler.close()

    def get_from_memory(self):
        file_handler = open(self.__file_location, 'r')
        input_info = file_handler.read()
        input_info = input_info.strip("\n")
        input_info = input_info.split("\n")
        for question in input_info:
            question = question.split(";")
            new_question = Question(int(question[0]), question[1], question[2], question[3], question[4], question[5], question[6])
            self.add_question(new_question)
        file_handler.close()

    def order_questions(self):
        sorted(self.__question_list, key=lambda question: question.difficulty, reverse=False)
