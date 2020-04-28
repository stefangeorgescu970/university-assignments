'''


@author: radu
'''
import traceback

from s02p1.domain import operations
from s02p1.domain.entities import create_student
from s02p1.domain.operations import add_student, delete_student, filter_students, \
    find_max_grade_student, validate_student


def ui_add_student(students, student_id, name, grade):
    try:
        student = create_student(int(student_id), name, int(grade))
        validate_student(student)
        add_student(students, student)
    except ValueError as ve:
        print("invalid input.", ve)
        raise ve        


def ui_print_student(student):
    print("(student_id={0}, name={1}, grade={2})".format(
        student["student_id"], student["name"], student["grade"]), end="\t")
     
 
def ui_print_all(students):
    if len(students) == 0:
        print("the list is empty.")
    for s in students:
        ui_print_student(s)
    print()


def ui_delete_student(students, student_id):
    delete_student(students, int(student_id))  # TODO data validation
        

def ui_filter(students, grade):
    ui_print_all(filter_students(students, int(grade)))  # TODO data validation


def ui_find_max_grade_student(students):
    ui_print_student(find_max_grade_student(students))
    print()
    
def find_students_by_name(students, t):
    ui_print_all(operations.find_students_by_name(students, t))
    
    
def read_cmd():
    command = input("command:")
    pos = command.find(" ")
    if(pos == -1):
        return (command, "")
    
    cmd = command[:pos]
    args = command[pos:]
    args = args.split(",")
    args = [e.strip() for e in args]
    
    return (cmd, args)


def run_app():
    students = []
    cmds = {"add":ui_add_student, "show":ui_print_all, "delete":ui_delete_student,
            "filter":ui_filter, "max":ui_find_max_grade_student,
            "find_by_name":find_students_by_name}
    while True:
        (cmd, args) = read_cmd()
        if cmd == "exit":
            break
        try:
            cmds[cmd](students, *args)
        except KeyError as ke:
            print("this command is not implemented.", ke)
        except Exception as ex:
            print("an error occurred; try again. " , ex)
            traceback.print_exc()

