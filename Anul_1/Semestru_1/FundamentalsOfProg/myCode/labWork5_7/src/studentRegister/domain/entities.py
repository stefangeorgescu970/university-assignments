class Student(object):

    def __init__(self, entity_id, name):
        '''
        Create a Student instance
        :param entity_id: The id of the student, integer
        :param name: The name of the student, string
        :return: Nada
        '''
        self.__entity_id = entity_id
        self.__name = name

    @property
    def entity_id(self):
        '''
        Getter for the student id
        '''
        return self.__entity_id

    @property
    def name(self):
        '''
        Getter for the student name
        '''
        return self.__name

    def __str__(self):
        '''
        Provide a string representation for a student
        :return: a string
        '''
        return "ID " + str(self.entity_id) + " is associated with the name " + self.name


class Discipline(object):

    def __init__(self, entity_id, name):
        '''
        Create a Discipline instance
        :param entity_id: an integer representing the id of the discipline
        :param name: A string containing the name of the discipline
        '''
        self.__entity_id = entity_id
        self.__name = name

    @property
    def entity_id(self):
        '''
        Getter for the discipline id
        '''
        return self.__entity_id

    @property
    def name(self):
        '''
        Getter for the discipline name
        :return:
        '''
        return self.__name

    def __str__(self):
        '''
        Provide a string representation for a discipline
        :return: a string
        '''
        return "ID " + str(self.entity_id) + " is associated with the discipline " + self.name


class Grade(object):

    def __init__(self, discipline_id, student_id, grade_value):
        '''
        Creates a Grade instance
        :param discipline_id: An int
        :param student_id: An int
        :param grade_value: An int
        :return:
        '''
        self.__entity_id = str(discipline_id) + '.' + str(student_id)
        self.__discipline_id = discipline_id
        self.__student_id = student_id
        self.__grade_value = grade_value

    @property
    def entity_id(self):
        return self.__entity_id

    @property
    def discipline_id(self):
        '''
        Getter for the id of the discipline
        '''
        return self.__discipline_id

    @property
    def student_id(self):
        '''
        Getter for the id of the student
        '''
        return self.__student_id

    @property
    def grade_value(self):
        '''
        Getter for the value of the grade
        '''
        return self.__grade_value

    def __str__(self):
        '''
        Provide a string representation for a grade
        :return: a string
        '''
        return "Student with the ID " + str(self.student_id) + " is graded with " + str(self.grade_value) + " at the discipline with the ID " + str(self.discipline_id)


class Link(object):
    def __init__(self, discipline_id, student_id):
        self.__discipline_id = discipline_id
        self.__student_id = student_id
        self.__entity_id = str(discipline_id) + '.' + str(student_id)

    @property
    def entity_id(self):
        return self.__entity_id

    @property
    def discipline_id(self):
        return self.__discipline_id

    @property
    def student_id(self):
        return self.__student_id

    def __str__(self):
        return "Student with the ID " + str(self.student_id) + " is enrolled at discipline with the ID " + str(self.discipline_id)


class Settings(object):
    def __init__(self, props_file):
        self.__props_file = props_file
        self.__root_directory = "/Users/Stefan/PycharmProjects/labWork5_7/"
        self.__repository = ""
        self.__student_file = ""
        self.__discipline_file = ""
        self.__ui = ""
        self.__set_settings()

    def __set_settings(self):
        setting_dict = self.__get_settings()
        self.__repository = setting_dict['repository']
        self.__student_file = self.__root_directory + setting_dict['students']
        self.__discipline_file = self.__root_directory + setting_dict['disciplines']
        self.__ui = setting_dict['ui']

    def __get_settings(self):
        file = open(self.__root_directory + self.__props_file, 'r')
        setting_dict = {}
        info = file.read()
        info.strip()
        info = info.split('\n')
        for setting in info:
            setting.strip()
            setting = setting.split('=')
            setting_dict[setting[0].strip()] = setting[1].strip()
        return setting_dict

    @property
    def repository(self):
        return self.__repository

    @property
    def student_file(self):
        return self.__student_file

    @property
    def discipline_file(self):
        return self.__discipline_file

    @property
    def ui(self):
        return self.__ui
