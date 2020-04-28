//
//  Console.hpp
//  Hospital_Departments
//
//  Created by Georgescu Stefan on 08/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#pragma once
#include "Controller.hpp"

class Console {
private:
    Controller my_controller;

public:
    void add_new_department();
    void run();
    void print_menu();
    void print_all();
    void print_efficient();
    void write_to_file();
    Console(Controller my_controller);
};
