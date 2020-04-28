"""
Created on 30/01/2017
@author Stefan
"""
from unittest import TestCase

from domain.entities import Sentence


class TestSentence(TestCase):
    def setUp(self):
        super().setUp()
        self.sentence = Sentence("anna has apples")

    def test_find_letter(self):
        self.assertEqual(True, self.sentence.find_letter('n'), "error at finding letter")
        self.assertEqual(False, self.sentence.find_letter('z'), "error at finding letter")

    def test_did_win(self):
        sent = Sentence("anna")
        self.assertEqual(False, sent.did_win(), "error at game end check")
        sent.find_letter("n")
        self.assertEqual(True, sent.did_win(), "error at game check")

    def test__str__(self):
        sent = Sentence("anna")
        self.assertEqual("a__a", str(sent), "Error at string")

    def test_hide_letters(self):
        self.assertEqual("a__a has a____s", str(self.sentence), "Error at hiding")

