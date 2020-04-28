//
//  HospitalDepartment.hpp
//  Hospital_Departments
//
//  Created by Georgescu Stefan on 08/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#pragma once
#include <string>

class HospitalDepartment {
protected:
    std::string hospital_name;
    int number_of_doctors;
    
public:
    HospitalDepartment(std::string hospital_name, int number_of_doctors);
    
    virtual bool is_efficient() = 0;
    
    virtual std::string to_string() = 0;
    
    std::string get_hospital();
};


class NeonatalUnit : public HospitalDepartment{
private:
    int number_of_mothers;
    int number_of_newborns;

public:
    double average_grade;
    
    NeonatalUnit(std::string hospital_name, int number_of_doctors, int number_of_mothers, int number_of_newborns, double average_grade);
    
    bool is_efficient() override;
    
    std::string to_string() override;
};


class Surgery : public HospitalDepartment {
private:
    int number_of_patients;
    
public:
    Surgery(std::string hospital_name, int number_of_doctors, int number_of_patients);
    
    bool is_efficient() override;
    
    std::string to_string() override;
};
