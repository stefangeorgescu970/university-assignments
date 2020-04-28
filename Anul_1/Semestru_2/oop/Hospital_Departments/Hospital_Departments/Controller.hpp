//
//  Controller.hpp
//  Hospital_Departments
//
//  Created by Georgescu Stefan on 08/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#pragma once
#include "HospitalDepartment.hpp"
#include <vector>
using namespace std;

class Controller {
private:
    vector<HospitalDepartment*> my_departments;
    
public:
    void add_department(HospitalDepartment* new_department);
    vector<HospitalDepartment*> get_all_departments();
    vector<HospitalDepartment*> get_all_efficient_departments();
    void write_to_file(string file_name);
    ~Controller();
};
