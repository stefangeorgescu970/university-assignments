//
//  GradeController.cpp
//  test_prep
//
//  Created by Georgescu Stefan on 18/06/2017.
//
//

#include "GradeController.hpp"
using namespace std;


GradeController::GradeController(GradeRepository& myRepository) : myRepository{}{
    this->myRepository = myRepository;
}

GradeController::GradeController() {}

vector<Student> GradeController::getMyStudents(){
    return this->myRepository.getMyStudents();
}

vector<Teacher> GradeController::getMyTeachers(){
    return this->myRepository.getMyTeacher();
}

void GradeController::addStudent(string name, int group){
    Student new_student{0, name, group};
    this->myRepository.addStudent(new_student);
}

void GradeController::deleteStudent(Student student){
    this->myRepository.deleteStudent(student);
}
