from unittest import TestCase

from studentRegister.controller.undo_controller import UndoController
from studentRegister.domain.validators import StudentValidator, LinkValidator, GradeValidator, DisciplineValidator
from studentRegister.repository.repository import Repository


class TestUndoController(TestCase):
    def setUp(self):
        super.setUp()
        self.__student_repo = Repository(StudentValidator)
        self.__link_repo = Repository(LinkValidator)
        self.__grade_repo = Repository(GradeValidator)
        self.__disc_repo = Repository(DisciplineValidator)
        self.__undo_controller = UndoController(self.__student_repo, self.__link_repo, self.__grade_repo, self.__disc_repo)


