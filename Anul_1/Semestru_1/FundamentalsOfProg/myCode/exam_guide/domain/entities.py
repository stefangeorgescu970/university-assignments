"""
Created on 28/01/2017
@author Stefan
"""


class Grade(object):
    def __init__(self, student_id, laboratory_no, laboratory_problem, value):
        self.__student_id = student_id
        self.__laboratory_no = laboratory_no
        self.__laboratory_problem = laboratory_problem
        self.__value = value

    @property
    def student_id(self):
        return self.__student_id

    @property
    def laboratory_no(self):
        return self.__laboratory_no

    @property
    def laboratory_problem(self):
        return self.__laboratory_problem

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return str(self.student_id) + " " + str(self.laboratory_no) + " " + str(self.laboratory_problem) + " " + str(self.value)


class Student(object):
    def __init__(self, id, name, group):
        self.__id = id
        self.__name = name
        self.__group = group

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def group(self):
        return self.__group

    def __str__(self):
        return "Student with ID " + str(self.id) + " is " + self.name + " and is in group " + self.group


class UndoObject(object):
    def __init__(self, identifier, calling_func, undo_func, *args):
        self.__identifier = identifier
        self.__calling_func = calling_func
        self.__undo_func = undo_func
        self.__args = args
        self.__did_undo = False
        self.__did_redo = False

    @property
    def identifier(self):
        return self.__identifier

    @property
    def caller(self):
        return self.__calling_func

    @property
    def handler(self):
        return self.__undo_func

    @property
    def args(self):
        return self.__args

    def do_undo(self):
        self.__did_undo = True

    def do_redo(self):
        self.__did_redo = True

    @property
    def did_undo(self):
        return self.__did_undo

    @property
    def did_redo(self):
        return self.__did_redo
