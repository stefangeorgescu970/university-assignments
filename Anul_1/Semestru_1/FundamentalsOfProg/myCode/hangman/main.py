"""
Created on 30/01/2017
@author Stefan
"""
from console.console import Console
from controller.controller import Controller
from domain.validator import SentenceValidator
from repository.repo import Repo

if __name__ == '__main__':
    # validator = SentenceValidator()
    # repo = Repo(validator, "/Users/Stefan/PycharmProjects/hangman/sentences.txt")
    # controller = Controller(repo)
    # console = Console(controller)
    # console.run()
    '''
    exemplu de comentariu
    '''



    x = 1
    for i in range(2, 200000):
        x = x * i
        print("currently multiplying with {0}".format(i))
    print(len(str(x)))