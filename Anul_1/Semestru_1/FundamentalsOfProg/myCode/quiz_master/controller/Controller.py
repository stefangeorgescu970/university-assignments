"""
Created on 29/01/2017
@author Stefan
"""
import random

from domain.Exceptions import ControllerException
from domain.entities import Question, Quiz


class Controller(object):
    def __init__(self, repo):
        self.__repo = repo

    def number_of_questions_for_difficulty(self, difficulty):
        number = 0
        question_list = self.__repo.get_all()
        for question in question_list:
            if question.difficulty == difficulty:
                number += 1
        return number

    def find_by_id(self, question_id):
        question_list = self.__repo.get_all()
        for question in question_list:
            if question_id == question.question_id:
                return question
        return None

    def add_question(self, question_id, text, answer1, answer2, answer3, correct_answer, difficulty):
        try:
            question_id = int(question_id)
            if self.find_by_id(question_id) is None:
                new_question = Question(question_id, text, answer1, answer2, answer3, correct_answer, difficulty)
                self.__repo.store(new_question)
            else:
                raise ControllerException("Duplicate ID {0}.".format(question_id))
        except ValueError:
            raise ControllerException("ID provided is not integer.")

    def get_all(self):
        return self.__repo.get_all()

    def get_difficulty(self, difficulty):
        question_list = self.__repo.get_all()
        req_question_list = []
        for question in question_list:
            if question.difficulty == difficulty:
                req_question_list.append(question)
        return req_question_list

    def get_not_difficulty(self, difficulty):
        question_list = self.__repo.get_all()
        req_question_list = []
        for question in question_list:
            if question.difficulty != difficulty:
                req_question_list.append(question)
        return req_question_list

    def add_questions_to_quiz(self, quiz):
        must_have_questions = self.get_difficulty(quiz.difficulty)
        for index in range(0, quiz.no_of_questions // 2):
            quiz.add_question(must_have_questions[index])
        how_many_left = quiz.no_of_questions - len(quiz)
        remain_list = self.get_not_difficulty(quiz.difficulty)
        for index in range(0, how_many_left):
            get_item = random.randint(0, len(remain_list) - 1)
            quiz.add_question(remain_list.pop(get_item))
        return quiz

    def create_quiz(self, difficulty, no_of_questions, file_name):
        try:
            no_of_questions = int(no_of_questions)
            available_questions = self.number_of_questions_for_difficulty(difficulty)
            if available_questions < no_of_questions // 2:
                raise ControllerException("Not enough {0} questions available.".format(difficulty))
            new_quiz = Quiz(difficulty, no_of_questions, file_name)
            final_quiz = self.add_questions_to_quiz(new_quiz)
            final_quiz.store()

        except ValueError:
            raise ControllerException("Number of questions must be an int.")

    def get_quiz_from_file(self, file_name):
        new_quiz = Quiz("", 0, file_name)
        new_quiz.get_from_memory()
        return new_quiz

    def play_quiz(self, file_name):
        points_dict = {'easy': 1, 'medium': 2, 'hard': 3}
        quiz = self.get_quiz_from_file(file_name)
        quiz.order_questions()
        points = 0
        question_list = quiz.get_questions()
        for question in question_list:
            print(question)
            answer = input("Provide your answer: ")
            if answer == question.correct_answer:
                points += points_dict[question.difficulty]
        print("Congrats, you got {0} points.".format(points))
