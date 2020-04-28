"""
Created on 07/12/2016
@author Stefan
"""
import pickle

from studentRegister.domain.entities import Student, Discipline


def create_pickle_files():
    students = [Student(1, "Stefan Georgescu"), Student(2, "Alexandru Nitu"), Student(3, "Alexandru Popescu"),
                Student(4, "Calin Badea"), Student(5, "Ana Calinescu")]
    disciplines = [Discipline(1, "Mathematics"), Discipline(2, "Computer Science")]
    student_file = open("/Users/Stefan/PycharmProjects/labWork5_7/Students.pickle", 'wb')
    disciplines_file = open("/Users/Stefan/PycharmProjects/labWork5_7/Disciplines.pickle", 'wb')
    pickle.dump(students, student_file)
    pickle.dump(disciplines, disciplines_file)
    student_file.close()
    disciplines_file.close()

create_pickle_files()