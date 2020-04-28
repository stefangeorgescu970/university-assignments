class RegisterException(Exception):
    pass


class InitException(Exception):
    pass


class StudentValidatorException(RegisterException):
    pass


class DisciplineValidatorException(RegisterException):
    pass


class StudentValidator(object):
    @staticmethod
    def validate(student):
        if not type(student.entity_id) is int:
            raise StudentValidatorException("ID must be an int.")

    # TODO - other student validations


class DisciplineValidator(object):
    @staticmethod
    def validate(discipline):
        if not type(discipline.entity_id) is int:
            raise DisciplineValidatorException("ID must be an int.")

    # TODO - other discipline validations


class GradeValidator(object):

    @staticmethod
    def validate(grade):
        pass

    # TODO - grade valitators


class LinkValidator(object):

    @staticmethod
    def validate(link):
        pass

    # TODO - link validators
