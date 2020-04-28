"""
@author: radu


"""


class UndoOperation(object):
    def __init__(self, source_method, handler, *args):
        self.__source_method = source_method
        self.__handler = handler
        self.__args = args

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
    def __init__(self):
        self.__operations = []

    @property
    def operations(self):
        return self.__operations

    def register_operation(self, source_method, handler, *args):
        self.__operations.append(UndoOperation(source_method, handler, *args))

    def undo(self):
        undo_operation = self.__operations.pop()  # TODO check for empty list
        undo_operation.handler(*undo_operation.args)
