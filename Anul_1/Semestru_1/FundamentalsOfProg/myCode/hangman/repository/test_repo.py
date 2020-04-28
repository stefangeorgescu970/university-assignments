"""
Created on 30/01/2017
@author Stefan
"""
from unittest import TestCase

from domain.entities import Sentence
from domain.exceptions import RepositoryException
from domain.validator import SentenceValidator
from repository.repo import Repo


class TestRepo(TestCase):
    def setUp(self):
        super().setUp()
        self.repo = Repo(SentenceValidator, "/Users/Stefan/PycharmProjects/hangman/sentence_test.txt")

    def test_init_from_file(self):
        self.assertEqual(3, len(self.repo.get_all()), "Error at initial value.")

    def test_store(self):
        self.repo.store(Sentence("ana are mere"))
        self.assertEqual(4, len(self.repo.get_all()), "Error after adding entity")
        self.assertRaises(RepositoryException, self.repo.store, Sentence("eu"))

    def test_get_all_string(self):
        string_list = self.repo.get_all_string()
        self.assertEqual(3, len(string_list), "Error at getting string list.")
        self.assertEqual("anna has apples", string_list[0], "Matching error.")

    def test_get_all(self):
        sentence_list = self.repo.get_all()
        self.assertEqual(3, len(sentence_list), "Error at getting sentence list.")
        cmp_sentence = Sentence("anna has apples")
        self.assertEqual(cmp_sentence.hidden, sentence_list[0].hidden, "Matching error.")
        self.assertEqual(cmp_sentence.string, sentence_list[0].string, "Matching error.")


