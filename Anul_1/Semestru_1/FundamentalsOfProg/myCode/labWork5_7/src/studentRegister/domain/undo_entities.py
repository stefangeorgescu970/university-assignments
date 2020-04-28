class Operation(object):
    def __init__(self, identifier, function_call, function_handler, args):
        self.__identifier = identifier
        self.__function_call = function_call
        self.__function_handler = function_handler
        self.__args = args

    @property
    def identifier(self):
        return self.__identifier

    @property
    def function_call(self):
        return self.__function_call

    @property
    def function_handler(self):
        return self.__function_handler

    @property
    def args(self):
        return self.__args


class RemovedGrades(object):
    def __init__(self, grades_list, add_grade, remove_grade):
        self.__grades_list = grades_list
        self.__add_grade = add_grade
        self.__remove_grade = remove_grade

    @property
    def grades_list(self):
        return self.__grades_list

    @property
    def add_grade(self):
        return self.__add_grade

    @property
    def remove_grade(self):
        return self.__remove_grade


class RemovedLinks(object):
    def __init__(self, link_list, add_link, remove_link):
        self.__link_list = link_list
        self.__add_link = add_link
        self.__remove_link = remove_link

    @property
    def link_list(self):
        return self.__link_list

    @property
    def add_link(self):
        return self.__add_link

    @property
    def remove_link(self):
        return self.__remove_link
