class NameAndGradeDTO(object):
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    @property
    def name(self):
        return self.__name

    @property
    def grade(self):
        return self.__grade


class NameAndGradeAssembler(object):
    @staticmethod
    def create_name_and_grade_dto(entity, grade):
        return NameAndGradeDTO(entity.name, grade)


class StudentAndDisciplineDTO(object):
    def __init__(self, discipline_name, student_name):
        self.__discipline_name = discipline_name
        self.__student_name = student_name

    @property
    def discipline_name(self):
        return self.__discipline_name

    @property
    def student_name(self):
        return self.__student_name


class StudentAndDisciplineAssembler(object):
    @staticmethod
    def create_student_and_discipline_dto(discipline, student):
        return StudentAndDisciplineDTO(discipline.name, student.name)


class StudentDisciplineGradeDTO(object):
    def __init__(self, student_name, discipline_name, grade_value):
        self.__student_name = student_name
        self.__disciplne_name = discipline_name
        self.__grade_value = grade_value

    @property
    def student_name(self):
        return self.__student_name

    @property
    def discipline_name(self):
        return self.__disciplne_name

    @property
    def grade_value(self):
        return self.__grade_value


class StudentDisciplineGradeAssembler(object):
    @staticmethod
    def create_student_discipline_grade_dto(student, discipline, grade_value):
        return StudentDisciplineGradeDTO(student.name, discipline.name, grade_value)
