//
//  Student.cpp
//  test_prep
//
//  Created by Georgescu Stefan on 18/06/2017.
//
//

#include "Student.hpp"
using namespace std;

Student::Student(int id, string name, int group, double grade, string nameOfGradingTeacher){
    this->id = id;
    this->name = name;
    this->group = group;
    this->grade = grade;
    this -> nameOfGradingTeacher = nameOfGradingTeacher;
}

int Student::getGroup(){
    return this->group;
}

string Student::getName(){
    return this->name;
}

double Student::getGrade(){
    return this->grade;
}

bool Student::operator==(const Student& rhs){
    if (this->name!= rhs.name)
        return false;
    if (this->group!=rhs.group)
        return false;
    return true;
}
