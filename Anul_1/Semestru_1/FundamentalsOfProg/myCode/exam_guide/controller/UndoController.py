"""
Created on 28/01/2017
@author Stefan
"""
from domain.entities import UndoObject


class UndoController(object):
    def __init__(self, student_controller, grade_controller):
        self.__student_controller = student_controller
        self.__grade_controller = grade_controller
        self.__last_operation = None

    def register_operation(self, identifier, caller, handler, *args):
        self.__last_operation = UndoObject(identifier, caller, handler, *args)

    def undo(self):
        if self.__last_operation.did_undo:
            print("You can only undo once.")
            return
        if self.__last_operation.identifier == 'as':
            self.__last_operation.handler(self.__last_operation.args[0])
            self.__last_operation.do_undo()

        elif self.__last_operation.identifier == 'rs':
            self.__last_operation.handler(self.__last_operation.args[0], self.__last_operation.args[1], self.__last_operation.args[2])
            self.__last_operation.do_undo()

        elif self.__last_operation.identifier == 'als':
            self.__last_operation.handler(self.__last_operation.args[0], self.__last_operation.args[1])
            self.__last_operation.do_undo()

        elif self.__last_operation.identifier == 'alg':
            self.__last_operation.handler(self.__last_operation.args[0], self.__last_operation.args[1], self.__last_operation.args[2])
            self.__last_operation.do_undo()

        elif self.__last_operation.identifier == 'gs':
            self.__last_operation.handler(self.__last_operation.args[0], self.__last_operation.args[1])
            self.__last_operation.do_undo()

    def redo(self):
        if not self.__last_operation.did_undo:
            print("There is nothing to redo.")
            return
        if self.__last_operation.did_redo:
            print("You can only redo once.")
            return
        if self.__last_operation.identifier == 'as':
            self.__last_operation.caller(self.__last_operation.args[0], self.__last_operation.args[1], self.__last_operation.args[2])
            self.__last_operation.do_redo()

        elif self.__last_operation.identifier == 'rs':
            self.__last_operation.caller(self.__last_operation.args[0])
            self.__last_operation.do_redo()

        elif self.__last_operation.identifier == 'als':
            self.__last_operation.caller(self.__last_operation.args[0], self.__last_operation.args[1], self.__last_operation.args[2])
            self.__last_operation.do_redo()

        elif self.__last_operation.identifier == 'alg':
            self.__last_operation.caller(self.__last_operation.args[0], self.__last_operation.args[1])
            self.__last_operation.do_redo()

        elif self.__last_operation.identifier == 'gs':
            self.__last_operation.caller(self.__last_operation.args[0], self.__last_operation.args[1], self.__last_operation.args[2])
            self.__last_operation.do_redo()