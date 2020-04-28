//
//  HospitalDepartment.cpp
//  Hospital_Departments
//
//  Created by Georgescu Stefan on 08/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include "HospitalDepartment.hpp"
using namespace std;


HospitalDepartment::HospitalDepartment(string hospital_name, int number_of_doctors){
    this->hospital_name = hospital_name;
    this->number_of_doctors = number_of_doctors;
}

NeonatalUnit::NeonatalUnit(string hospital_name, int number_of_doctors, int number_of_mothers, int number_of_newborns, double average_grade) : HospitalDepartment(hospital_name, number_of_doctors){
    this->number_of_mothers = number_of_mothers;
    this->number_of_newborns = number_of_newborns;
    this->average_grade = average_grade;
}

Surgery::Surgery(string hospital_name, int number_of_doctors, int number_of_patients) : HospitalDepartment(hospital_name, number_of_doctors){
    this->number_of_patients = number_of_patients;
}

bool NeonatalUnit::is_efficient(){
    if(this->average_grade > 8.5 and this->number_of_newborns >= this->number_of_mothers)
        return true;
    return false;
}

bool Surgery::is_efficient(){
    if((this->number_of_patients / this->number_of_doctors) >= 2)
        return true;
    return false;
}

string NeonatalUnit::to_string(){
    string result;
    result += "NeonatalUnit: ";
    result += this->hospital_name;
    result += " ";
    result += ::to_string(this->number_of_doctors);
    result += " ";
    result += ::to_string(this->number_of_newborns);
    result += " ";
    result += ::to_string(this->number_of_mothers);
    result += " ";
    result += ::to_string(this->average_grade);
    return result;
}

string Surgery::to_string(){
    string result;
    result += "Surgery: ";
    result += this->hospital_name;
    result += " ";
    result += ::to_string(this->number_of_doctors);
    result += " ";
    result += ::to_string(this->number_of_patients);
    return result;
}

string HospitalDepartment::get_hospital(){
    return this->hospital_name;
}
