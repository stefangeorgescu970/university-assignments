"""
Created on 28/01/2017
@author Stefan
"""
import traceback

from console.console import Console
from controller.GradeController import GradeController
from controller.StudentController import StudentController
from controller.UndoController import UndoController
from domain.validators import GradeValidator, StudentValidator
from repository.GradeRepo import GradeRepo
from repository.StudentRepo import StudentRepo

if __name__ == '__main__':
    print("App started running.")

    grade_validator = GradeValidator()
    student_validator = StudentValidator()

    grade_repo = GradeRepo(grade_validator)
    student_repo = StudentRepo(student_validator)

    grade_controller = GradeController(grade_repo)
    student_controller = StudentController(student_repo)
    undo_controller = UndoController(student_controller, grade_controller)

    console = Console(student_controller, grade_controller, undo_controller)

    try:
        console.run()
    except Exception:
        print("An error accured.")
        traceback.print_exc()

    print("That's all folks.")

