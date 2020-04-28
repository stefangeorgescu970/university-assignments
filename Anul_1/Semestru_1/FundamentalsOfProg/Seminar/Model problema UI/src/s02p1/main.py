'''


@author: radu


Write an application which manages the students of a faculty. 
Each student has a unique id, a name and a grade. The application should 
allow to:

F1: print all students 
F2: add students
F3: delete students
F4: show students whose grades are >= a given value
F5: find a student with the maximal grade
F6_: split the application into modules (main, ui, domain, util)
F7_: validate input data
F8_: student_id is unique - validation in add, delete etc.
F9: find all students whose name contain a string t (the match should not be
    case sensitive)  
F10: undo
F11: remove all students with the grade smaller than 5 (using TDD)
F12: sort students according to their grade (descending)  (using TDD)
F13: given an integer 'nr', find the top nr students according 
     to their grade  (using TDD)
F14: compute the average grade of all students having the grade >= 5 (using TDD)
F15: sort all students according to their grade and alphabetically (using TDD). 
------------

I1: F1, F2, F3, F4, F5
I2: F6_, F7_
I3: F8_, F9
I4: F10
I5: F11, F12, F13, F14, F15
'''
from _functools import reduce

#=============================================domain================================================

def create_student(student_id, name, grade):
    return {"student_id":student_id, "name":name, "grade":grade}

def get_student_id(student):
    return student["student_id"]

def get_name(student):
    return student["name"]

def get_grade(student):
    return student["grade"]

def add_student(students, student):
    students.append(student)
    
def delete_student(students, student_id):    
    students[:] = [s for s in students if get_student_id(s) != student_id]

def filter_students(students, grade):
    return list(filter(lambda s: get_grade(s) >= grade, students))

def find_max_grade_student(students):
    return reduce(lambda x, y:x if get_grade(x) > get_grade(y) else y, students)

#=============================================ui================================================

def ui_print_student(student):
    print("(student_id={0}, name={1}, grade={2})".format(
        student["student_id"], student["name"], student["grade"]), end="\t")
    

def ui_print_all(students):
    if len(students) == 0:
        print("the list is empty.")
    for s in students:
        ui_print_student(s)
    print()
    
def print_options():
    print("1 - add student\n\
2 - print students\n\
3 - delete students\n\
4 - filter students by grade\n\
5 - max grade student\n\
x - exit")
    
def run_menu():    
    students = []
    options = {1:ui_add_student, 2:ui_print_all, 3:ui_delete_student, 4:ui_filter_students, 
               5:ui_find_max_grade_student}
    
    while True:
        print_options()
        option = input("option=")
        if option == "x":
            break
        try:            
            option = int(option)
            options[option](students)
        except ValueError as ve:
            print("invalid input.", ve)
        except KeyError as ke:
            print("option not yet implemented.", ke)    


def ui_add_student(students):
    student_id = int(input("student_id="))
    name = input("name = ")
    grade = int(input("grade="))
    
    student = create_student(student_id, name, grade)
    add_student(students, student)
    
def ui_delete_student(students):
    student_id = int(input("student_id="))
    delete_student(students, student_id)
    
def ui_filter_students(students):
    grade = int(input("grade="))
    print(filter_students(students, grade))     
    
def ui_find_max_grade_student(students):
    print(find_max_grade_student(students))
    


#=============================================test==============================================

def setUp():
    students = []
    students.append(create_student("sid1", "sn1", 10))
    students.append(create_student("sid2", "sn2", 9))
    return students
    




def test_add_student():
    l = setUp()
    assert(len(l) == 2)
    
    add_student(l, create_student("sid3", "sn3", 9))
    assert(len(l) == 3)
    
def test_all():
    test_add_student()


if __name__ == '__main__':
    test_all()
    
    run_menu()
    
    print("hello")
    
    
    
    
