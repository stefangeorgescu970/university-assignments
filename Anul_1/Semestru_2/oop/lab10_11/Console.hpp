//
//  Console.hpp
//  lab5_6
//
//  Created by Georgescu Stefan on 27/03/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#pragma once
#include "Controller.hpp"

class Console{
private:
    Controller my_controller;
    void run_administrator();
    void print_administrator_menu();
    void run_user();
    void print_user_menu();
    void add();
    void remove();
    void update();
    void list_all();
    void go_through_shop();
    void print_sock(Socks current_sock);
    void display_shopping_cart();
public:
    
    Console(Controller my_controller);
    Console();
    void run();
};
