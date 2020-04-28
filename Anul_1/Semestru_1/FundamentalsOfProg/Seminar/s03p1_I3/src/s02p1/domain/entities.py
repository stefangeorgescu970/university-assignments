'''

@author: radu
'''

def create_student(student_id, name, grade):
    return {"student_id":student_id, "name":name, "grade":grade}

def get_student_id(student):
    return student["student_id"]

def get_name(student):
    return student["name"]

def get_grade(student):
    return student["grade"]

def set_student_id(student, student_id):
    student["student_id"] = student_id
    
def set_name(student, name):
    student["name"] = name
    
def set_grade(student, grade):
    student["grade"] = grade