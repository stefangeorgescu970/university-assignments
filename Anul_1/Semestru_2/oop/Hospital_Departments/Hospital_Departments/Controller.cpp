//
//  Controller.cpp
//  Hospital_Departments
//
//  Created by Georgescu Stefan on 08/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include "Controller.hpp"
#include <fstream>

void Controller::add_department(HospitalDepartment* new_department){
    this->my_departments.push_back(new_department);
}

vector<HospitalDepartment*> Controller::get_all_departments(){
    return this->my_departments;
}

vector<HospitalDepartment*> Controller:: get_all_efficient_departments(){
    vector<HospitalDepartment*> result;
    for(HospitalDepartment* dep : this->my_departments)
        if (dep->is_efficient())
            result.push_back(dep);
    return result;
}

bool comp(HospitalDepartment* h1, HospitalDepartment* h2){
    if(h1->get_hospital() < h2->get_hospital())
        return true;
    return false;
}

void Controller::write_to_file(string file_name){
    ofstream fout (file_name);
    vector<HospitalDepartment*> sorted = this->my_departments;
    sort(sorted.begin(), sorted.end(), &comp);
    for(HospitalDepartment* dep : sorted){
        fout<<dep->to_string();
        if(dep->is_efficient()) fout<<" is efficient.\n";
        else fout<<" is not efficient.\n";
    }
    fout.close();
}

Controller::~Controller(){
    for(HospitalDepartment* dep : this->my_departments)
        free(dep);
}
