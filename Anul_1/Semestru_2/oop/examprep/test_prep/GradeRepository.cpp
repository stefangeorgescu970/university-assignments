//
//  GradeRepository.cpp
//  test_prep
//
//  Created by Georgescu Stefan on 18/06/2017.
//
//

#include "GradeRepository.hpp"
#include <fstream>
#include <iostream>
using namespace std;

GradeRepository::GradeRepository() {}

GradeRepository::GradeRepository(string studentFileName, string teacherFileName){
    this->initStudentData(studentFileName);
    this->initTeacherData(teacherFileName);
    
    
}

void GradeRepository::initStudentData(std::string studentFileName){
    ifstream studIn (studentFileName);
    int id, group;
    double grade;
    string surName, firstName, surNameOfGradingTeacher, firstNameOfGradingTeacher;
    while (!studIn.eof()) {
        studIn>>id>>surName>>firstName>>group>>grade>>surNameOfGradingTeacher>>firstNameOfGradingTeacher;
        Student newStudent{id, firstName+" "+surName, group, grade, firstNameOfGradingTeacher+" "+surNameOfGradingTeacher};
        this->myStudents.push_back(newStudent);
    }
    studIn.close();
}



vector<string> tokenize (const char *str, char c = ' '){
    vector<string> result;
    do
    {
        const char *begin = str;
        while(*str != c && *str)
            str++;
        result.push_back(string(begin, str));
    } while (0 != *str++);
    return result;
}


void GradeRepository::initTeacherData(std::string teacherFileName){
    ifstream teachIn (teacherFileName);
    char line[100];
    while (teachIn.getline(line, 99)) {
        vector<string> input = tokenize(line);
        Teacher newTeacher{input[1]+" "+input[0]};
        for(int index = 2; index < (int)input.size(); index++){
            newTeacher.addGroupICanGrade(stoi(input[index]));
        }
        this->myTeachers.push_back(newTeacher);
    }
    teachIn.close();
}

vector<Student> GradeRepository::getMyStudents(){
    return this->myStudents;
}

vector<Teacher> GradeRepository::getMyTeacher(){
    return this->myTeachers;
}

void GradeRepository::addStudent(Student new_student){
    this->myStudents.push_back(new_student);
}

void GradeRepository::deleteStudent(Student student){
    this->myStudents.erase(find(myStudents.begin(), myStudents.end(), student));
}


