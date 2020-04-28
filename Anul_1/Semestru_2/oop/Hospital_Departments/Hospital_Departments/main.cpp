//
//  main.cpp
//  Hospital_Departments
//
//  Created by Georgescu Stefan on 08/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include <iostream>
#include "Console.hpp"
using namespace std;

int main() {
    
    Controller my_controller;
    Console my_console{my_controller};
    my_console.run();
}
