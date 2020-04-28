from unittest import TestCase

from studentRegister.controller.statistics_controller import StatisticsController
from studentRegister.domain.validators import LinkValidator, GradeValidator, DisciplineValidator
from studentRegister.domain.validators import StudentValidator
from studentRegister.repository.repository import Repository


class TestStatisticsController(TestCase):
    def setUp(self):
        super.setUp()
        self.__student_repo = Repository(StudentValidator)
        self.__link_repo = Repository(LinkValidator)
        self.___repo = Repository(GradeValidator)
        self.__disc_repo = Repository(DisciplineValidator)
        self.__undo_controller = StatisticsController(self.__student_repo, self.__link_repo, self.__grade_repo, self.__disc_repo)


