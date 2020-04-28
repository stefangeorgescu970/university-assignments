'''

@author: radu
'''
from s02p1.domain.entities import create_student
from s02p1.domain.operations import add_student


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
    
def test_delete_student():
    pass


#=======================================================================================================

def test_all_operations():
    test_add_student()
    test_delete_student()
    
    