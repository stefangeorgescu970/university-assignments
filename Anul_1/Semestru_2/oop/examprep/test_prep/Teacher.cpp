//
//  Teacher.cpp
//  test_prep
//
//  Created by Georgescu Stefan on 18/06/2017.
//
//

#include "Teacher.hpp"
using namespace std;

Teacher::Teacher(string name) {
    this->name = name;
}

void Teacher::addGroupICanGrade(int group){
    this->groupsICanGrade.push_back(group);
}

string Teacher::getName(){
    return this->name;
}

vector<int> Teacher::getGroups(){
    return this->groupsICanGrade;
}
