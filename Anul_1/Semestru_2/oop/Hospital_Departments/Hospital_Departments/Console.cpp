//
//  Console.cpp
//  Hospital_Departments
//
//  Created by Georgescu Stefan on 08/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include "Console.hpp"
#include <iostream>
#include <exception>

void Console::add_new_department(){
    string dep_type, hosptial_name;
    int number_of_doctors;
    cout<<"Department type: ";
    cin >> dep_type;
    cout<<"Hospital name: ";
    cin>>hosptial_name;
    cout<<"Number of doctors: ";
    cin>>number_of_doctors;
    if(dep_type == "Surgery"){
        int no_of_patients;
        cout<<"Number of patients: ";
        cin>>no_of_patients;
        HospitalDepartment* new_department = new Surgery{hosptial_name, number_of_doctors, no_of_patients};
        this->my_controller.add_department(new_department);
        if (new_department->is_efficient()) {
            cout<<"Department is efficient.\n\n";
        } else {
            cout<<"Department is not efficient.\n\n";
        }
    } else if (dep_type == "Neonatal") {
        int no_of_mothers, no_of_newborns;
        double average_grade;
        cout<<"Number of mothers: ";
        cin>>no_of_mothers;
        cout<<"Number of newborns: ";
        cin>>no_of_newborns;
        cout<<"Average grade: ";
        cin>>average_grade;
        HospitalDepartment* new_department = new NeonatalUnit{hosptial_name, number_of_doctors, no_of_mothers, no_of_newborns, average_grade};
        this->my_controller.add_department(new_department);
        if (new_department->is_efficient()) {
            cout<<"Department is efficient.\n\n";
        } else {
            cout<<"Department is not efficient.\n\n";
        }
    } else
        throw exception();

}

void Console::print_menu(){
    cout<<"1. Add a new department.\n";
    cout<<"2. Show all departments in the country.\n";
    cout<<"3. Show all the efficient departments in the country.\n";
    cout<<"4. Save all the departments in a file.\n";
    cout<<"5. Exit.\n\n";
}

void Console::print_all(){
    vector<HospitalDepartment*> my_departments = this->my_controller.get_all_departments();
    for(HospitalDepartment* dept : my_departments){
        string to_print = dept->to_string();
        cout<<to_print<<endl;
    }
}

void Console::print_efficient(){
    vector<HospitalDepartment*> my_efficient_depts = this->my_controller.get_all_efficient_departments();
    for(HospitalDepartment* dept : my_efficient_depts){
        string to_print = dept->to_string();
        cout<<to_print<<endl<<endl;
    }
    cout<<endl;
}

void Console::write_to_file(){
    string file_name;
    cout<<"Input file name: ";
    cin>>file_name;
    this->my_controller.write_to_file(file_name);
}

void Console::run(){
    HospitalDepartment* dept_n = new NeonatalUnit("Aurel", 3, 5, 12, 6);
    HospitalDepartment* dept_s = new Surgery("Vlaicu", 5, 12);
    this->my_controller.add_department(dept_n);
    this->my_controller.add_department(dept_s);
    while (true) {
        this->print_menu();
        int option;
        cout<<"Enter option: ";
        cin>>option;
        switch (option) {
            case 1:{
                try {
                    this->add_new_department();
                } catch (exception& exc) {
                    cout<<"Wrong department type provided.\n\n";
                }
                break;
            }
            case 2:{
                this->print_all();
                break;
            }
            case 3:{
                this->print_efficient();
                break;
            }
            case 4:{
                this->write_to_file();
                break;
            }
            case 5:{
                cout<<"Buh bye!\n";
                return;
            }
            default:{
                cout<<"Option not available.\n\n";
            }
        }
    }
}


Console::Console(Controller my_controller){
    this->my_controller = my_controller;
}



