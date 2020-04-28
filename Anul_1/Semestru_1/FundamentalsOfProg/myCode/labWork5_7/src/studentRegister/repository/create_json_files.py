"""
Created on 07/12/2016
@author Stefan
"""
import json

from studentRegister.domain.entities import Discipline
from studentRegister.domain.entities import Student


def create_json_files():
    students = {1: "Stefan Georgescu", 2: "Alexandru Nitu", 3:"Alexandru Popescu",
                4: "Calin Badea", 5: "Ana Calinescu"}
    disciplines = {1:"Mathematics", 2:"Computer Science"}

    student_file = open("/Users/Stefan/PycharmProjects/labWork5_7/Students.json", 'w')
    discipline_file = open("/Users/Stefan/PycharmProjects/labWork5_7/Disciplines.json", 'w')
    json.dump(students, student_file)
    json.dump(disciplines, discipline_file)
    student_file.close()
    discipline_file.close()

create_json_files()
