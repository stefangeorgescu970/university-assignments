//
//  main.cpp
//  lab5_6
//
//  Created by Georgescu Stefan on 22/03/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include <iostream>
#include "Console.hpp"
#include "Tests.hpp"
#include "GUI.hpp"
#include <QtWidgets/QApplication>

using namespace std;

int main(int argc, char *argv[]) {
    
    Tests::test_all();
    QApplication a(argc, argv);
    int file_type;
    cout<<"Enter 1 for CSV and 2 for HTML: ";
    cin>>file_type;
    if(cin.fail()){
        cout<<"You did not enter an integer. Program stopping.\n\n";
        cin.clear();
        cin.ignore();
        return 0;
    }
    if(file_type == 1){
        RepositoryCSV* my_repository = new RepositoryCSV{"basket_CSV.csv","/Users/Stefan/Documents/Facultate/Anul_1/Semestru_2/Object_Oriented_Programming/lab10_11/socks.txt"};
        Controller* my_controller = new Controller{my_repository};
//        Console my_console{my_controller};
//        my_console.run();
        SockShopQt my_gui{my_controller};
        my_gui.show();
        return a.exec();
    } else if (file_type == 2) {
        RepositoryHTML* my_repository = new RepositoryHTML{"basket_html.html", "/Users/Stefan/Documents/Facultate/Anul_1/Semestru_2/Object_Oriented_Programming/lab10_11/socks.txt"};
        Controller* my_controller = new Controller{my_repository};
//        Console my_console{my_controller};
//        my_console.run();
        SockShopQt my_gui{my_controller};
        my_gui.show();
        return a.exec();
    } else {
        cout<<"Try harder next time.\n";
        return 0;
    }
}
