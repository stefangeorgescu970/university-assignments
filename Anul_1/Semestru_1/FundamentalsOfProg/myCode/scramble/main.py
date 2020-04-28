"""
Created on 29/01/2017
@author Stefan
"""
from console.console import Console
from controller.Controller import Controller
from controller.UndoController import UndoController
from repository.SentenceRepository import SentenceRepository

if __name__ == '__main__':
    sentence_repo = SentenceRepository()
    controller = Controller(sentence_repo)
    undo_controller = UndoController()
    console = Console(controller, undo_controller)
    console.run()

