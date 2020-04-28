"""
@author: radu


"""
from enum import Enum


def delete_product_handler(product_controller, *args):
    product_controller.delete_product(args[0])


class UndoHandlers(Enum):
    DELETE_PRODUCT_HANDLER = delete_product_handler


def undoable(handler):
    def decorate(f):
        def decorated_f(self, *args):
            f(self, *args)
            UndoController.register_operation(self, f, handler, *args)

        return decorated_f

    return decorate


class UndoOperation(object):
    def __init__(self, controller, source_method, handler, *args):
        self.__controller = controller
        self.__source_method = source_method
        self.__handler = handler
        self.__args = args

    @property
    def controller(self):
        return self.__controller

    @property
    def source_method(self):
        return self.__source_method

    @property
    def handler(self):
        return self.__handler

    @property
    def args(self):
        return self.__args


class UndoController(object):
    __operations = []

    @classmethod
    def register_operation(cls, controller, source_method, handler, *args):
        cls.__operations.append(UndoOperation(controller, source_method, handler, *args))

    @classmethod
    def undo(cls):
        undo_operation = cls.__operations.pop()  # TODO check for empty list
        undo_operation.handler(undo_operation.controller, *undo_operation.args)
