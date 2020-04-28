"""
Created on 30/01/2017
@author Stefan
"""


class SentenceValidator(object):
    @staticmethod
    def validate(sentence):
        """
        Validates if a sentence respects the conditions: at least one word, every word larger than 3 chars
        :param sentence:
        :return: True if conditions, False otherwise
        """
        sentence = sentence.string.split(' ')
        if len(sentence) == 0:
            return False
        for word in sentence:
            if len(word) < 3:
                return False
        return True
