import traceback
from tkinter import *

from studentRegister.controller.discipline_controller import DisciplineController
from studentRegister.controller.grade_controller import GradeController
from studentRegister.controller.link_controller import LinkController
from studentRegister.controller.statistics_controller import StatisticsController
from studentRegister.controller.student_controller import StudentController
from studentRegister.controller.undo_controller import UndoController
from studentRegister.domain.entities import Settings
from studentRegister.domain.validators import StudentValidator, DisciplineValidator, GradeValidator, LinkValidator, \
    InitException
from studentRegister.repository.DisciplineFileRepository import DisciplineFileRepository
from studentRegister.repository.DisciplineJsonRepository import DisciplineJsonRepository
from studentRegister.repository.DisciplinePickleRepository import DisciplinePickleRepository
from studentRegister.repository.StudentFileRepository import StudentFileRepository
from studentRegister.repository.StudentJsonRepository import StudentJsonRepository
from studentRegister.repository.StudentPickleRepository import StudentPickleRepository
from studentRegister.repository.repository import Repository
from studentRegister.repository.undo_repository import OperationsRepository
from studentRegister.ui.console import Console
from studentRegister.ui.gui import GUI
from studentRegister.ui.ui_handlers import UiHandleStudentCommands, UiHandleDisciplineCommands, UiHandleLinkCommands, \
    UiHandleGradeCommands, UiHandleStatisticsCommands, UiHandleUndoCommands

if __name__ == "__main__":
    print("App started running.")

    try:
        settings_file = Settings("settings.properties")
        repository = settings_file.repository
        if repository == "inmemory":
            student_repository = Repository(StudentValidator)
            discipline_repository = Repository(DisciplineValidator)
        elif repository == "textfiles":
            student_file = settings_file.student_file
            discipline_file = settings_file.discipline_file
            student_repository = StudentFileRepository(StudentValidator, student_file)
            discipline_repository = DisciplineFileRepository(DisciplineValidator, discipline_file)
        elif repository == "binaryfiles":
            student_file = settings_file.student_file
            discipline_file = settings_file.discipline_file
            student_repository = StudentPickleRepository(StudentValidator, student_file)
            discipline_repository = DisciplinePickleRepository(DisciplineValidator, discipline_file)
        elif repository == "jsonfiles":
            student_file = settings_file.student_file
            discipline_file = settings_file.discipline_file
            student_repository = StudentJsonRepository(StudentValidator, student_file)
            discipline_repository = DisciplineJsonRepository(DisciplineValidator, discipline_file)
        else:
            raise InitException("Repository type {0} not available".format(repository))
        grade_repository = Repository(GradeValidator)
        link_repository = Repository(LinkValidator)
        undo_repository = OperationsRepository()
        redo_repository = OperationsRepository()

        discipline_controller = DisciplineController(discipline_repository)
        student_controller = StudentController(student_repository)
        grade_controller = GradeController(student_repository, discipline_repository, grade_repository)
        link_controller = LinkController(student_repository, discipline_repository, link_repository)
        statistics_controller = StatisticsController(student_repository, discipline_repository, link_repository, grade_repository)
        undo_controller = UndoController(undo_repository, redo_repository)

        ui_student_command = UiHandleStudentCommands(student_controller, link_controller, grade_controller, undo_controller)
        ui_discipline_command = UiHandleDisciplineCommands(discipline_controller, link_controller, grade_controller, undo_controller)
        ui_link_command = UiHandleLinkCommands(student_controller, discipline_controller, link_controller, undo_controller)
        ui_grade_command = UiHandleGradeCommands(student_controller, discipline_controller, link_controller, grade_controller, undo_controller)
        ui_statistics_command = UiHandleStatisticsCommands(discipline_controller, statistics_controller)
        ui_undo_command = UiHandleUndoCommands(undo_controller)

        user_interface = settings_file.ui

        if user_interface == "console":
            running = Console(ui_student_command, ui_discipline_command, ui_link_command, ui_grade_command, ui_statistics_command, ui_undo_command)
            running.run_console()
        elif user_interface == "gui":
            root = Tk()
            running = GUI(root, student_controller, discipline_controller, link_controller, grade_controller, statistics_controller, undo_controller)
            root.mainloop()
        else:
            raise InitException("User interface type {0} not available".format(user_interface))
    except KeyError:
        print("Faulty settings file.")
    except InitException as ie:
        print(ie)
    except Exception as e:
        print(e)
        traceback.print_exc()
    print("That's all folks!")
