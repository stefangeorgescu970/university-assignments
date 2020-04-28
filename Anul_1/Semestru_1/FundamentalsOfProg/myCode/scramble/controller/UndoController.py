"""
Created on 29/01/2017
@author Stefan
"""


class UndoController(object):
    def __init__(self):
        self.__last_operation = None

    def register_operation(self, undo_object):
        self.__last_operation = undo_object

    def undo(self):
        self.__last_operation.undo()

