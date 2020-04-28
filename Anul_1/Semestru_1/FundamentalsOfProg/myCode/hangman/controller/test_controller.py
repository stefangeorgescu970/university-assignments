"""
Created on 30/01/2017
@author Stefan
"""

from controller import Controller
from domain.entities import Sentence
from domain.exceptions import ControllerException
from domain.validator import SentenceValidator
from repository.repo import Repo


from unittest import TestCase


class TestController(TestCase):
    def setUp(self):
        super().setUp()
        self.repo = Repo(SentenceValidator, "/Users/Stefan/PycharmProjects/hangman/sentence_test.txt")
        self.controller = Controller(self.repo)

    def test_add(self):
        self.assertEqual(len(self.repo.get_all()), 3, "Error at loading")
        self.controller.add("planes are quick")
        self.assertEqual(len(self.repo.get_all()), 4, "Error at adding")
        self.assertRaises(ControllerException, self.controller.add, "planes are quick")

    def test_get_random_sentence(self):
        random_sentence = self.controller.get_random_sentence()
        self.assertEqual(type(random_sentence), Sentence, "Fail at getting random")

    def test_get_available_letters(self):
        sentence = Sentence("anna has apples")
        char_list = self.controller.get_available_letters(sentence)
        self.assertEqual(True, 'a' in char_list, "fail at getting letter")
        self.assertEqual(True, 'h' in char_list, "fail at getting letter")
        self.assertEqual(True, 's' in char_list, "fail at getting letter")
