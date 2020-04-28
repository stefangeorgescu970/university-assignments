//
//  Console.cpp
//  lab5_6
//
//  Created by Georgescu Stefan on 27/03/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include "Console.hpp"
#include <iostream>
#include <string>
#include "Exceptions.cpp"
using namespace std;

Console::Console(Controller my_controller) : my_controller(my_controller){
}

Console::Console() : my_controller{}{
    
}

void Console::add(){
    int size, price, quantity;
    string colour, photograph;
    cout<<"Enter the size of the socks: ";
    cin>>size;
    if(cin.fail()){
        cout<<"You did not enter an integer. Operation stopping.\n\n";
        cin.clear();
        cin.ignore();
        return;
    }
    cout<<"Enter the colour of the socks: ";
    cin.get();
    getline(cin, colour);
    cout<<"Enter the price of the socks: ";
    cin>>price;
    if(cin.fail()){
        cout<<"You did not enter an integer. Operation stopping.\n\n";
        cin.clear();
        cin.ignore();
        return;
    }
    cout<<"Enter the quantity of the socks: ";
    cin>>quantity;
    if(cin.fail()){
        cout<<"You did not enter an integer. Operation stopping.\n\n";
        cin.clear();
        cin.ignore();
        return;
    }
    cout<<"Enter a link for the picture of the socks: ";
    cin.get();
    getline(cin, photograph);
    
    try {
        this->my_controller.add(size, price, quantity, colour, photograph);
        cout<<"Add successful.\n\n";
    } catch (RepositoryException& exc) {
        cout<<exc.what();
    }
}

void Console::remove(){
    int size;
    string colour;
    cout<<"Enter the size of the socks you want to remove: ";
    cin>>size;
    if(cin.fail()){
        cout<<"You did not enter an integer. Operation stopping.\n\n";
        cin.clear();
        cin.ignore();
        return;
    }
    cout<<"Enter the colour of the socks you want to remove: ";
    cin.get();
    getline(cin, colour);
    try {
        this->my_controller.remove(size, colour);
        cout<<"Remove successful.\n\n";
    } catch (RepoRemoveException& exc) {
        cout<<exc.what();
    }
}

void Console::update(){
    int size;
    string colour;
    cout<<"Enter the size of the socks you want to update: ";
    cin>>size;
    if(cin.fail()){
        cout<<"You did not enter an integer. Operation stopping.\n\n";
        cin.clear();
        cin.ignore();
        return;
    }
    cout<<"Enter the colour of the socks you want to update: ";
    cin.get();
    getline(cin, colour);
    cout<<"1. Update the quantity.\n";
    cout<<"2. Update the price.\n";
    int decision;
    if(cin.fail()){
        cout<<"You did not enter an integer. Operation stopping.\n\n";
        cin.clear();
        cin.ignore();
        return;
    }
    cout<<"Enter number corresponding to what you want to update: ";
    cin>>decision;
    try{
    if (decision == 1) {
        int new_quantity;
        cout<<"Enter the new quantity: ";
        cin>>new_quantity;
        if(cin.fail()){
            cout<<"You did not enter an integer. Operation stopping.\n\n";
            cin.clear();
            cin.ignore();
            return;
        }
        this->my_controller.update_quantity(size, colour, new_quantity);
    } else if (decision == 2) {
        int new_price;
        cout<<"Enter the new price: ";
        cin>>new_price;
        if(cin.fail()){
            cout<<"You did not enter an integer. Operation stopping.\n\n";
            cin.clear();
            cin.ignore();
            return;
        }
        this->my_controller.update_price(size, colour, new_price);
    } else {
        cout<<"Option not available.\n\n";
    }
    cout<<"Product updated with ease.\n\n";
    } catch (RepoUpdateException& exc) {
        cout<<exc.what();
    }
}

void Console::print_sock(Socks current_sock){
    cout<<"Size: "<<current_sock.get_size()<<endl;
    cout<<"Price: "<<current_sock.get_price()<<endl;
    cout<<"Quantity: "<<current_sock.get_quantity()<<endl;
    cout<<"Colour: "<<current_sock.get_colour()<<endl;
    cout<<"Link to photo: "<<current_sock.get_photograph()<<"\n\n";
}

void Console::list_all(){
    if(this->my_controller.get_length() == 0){
        cout<<"No socks here bruh.\n\n";
        return;
    }
    vector<Socks> my_products = this->my_controller.get_products();
    for(Socks& current_sock:my_products) {
        cout<<"Socks number " << &current_sock - &my_products[0] + 1<<endl;
        this->print_sock(current_sock);
    }
}

void Console::print_administrator_menu(){
    cout<<"1. Add a new pair of socks.\n";
    cout<<"2. Remove a pair of socks.\n";
    cout<<"3. Update information on an existing pair of socks.\n";
    cout<<"4. List all socks in the store.\n";
    cout<<"5. Go one layer up in the application.\n";
}

void Console::run_administrator(){
    bool running = true;
    while (running) {
        this->print_administrator_menu();
        cout<<"Please enter an option: ";
        int funcs;
        cin>>funcs;
        if(cin.fail()){
            cout<<"You did not enter an integer.\n\n";
            cin.clear();
            cin.ignore();
        } else {
            if (funcs == 1) {
                this->add();
            } else if (funcs == 2) {
                this->remove();
            } else if (funcs == 3) {
                this->update();
            } else if (funcs == 5) {
                running = false;
            } else if (funcs == 4) {
                this->list_all();
            } else {
                cout<<"Option not available.\n\n";
            }
        }
    }
}

void Console::go_through_shop(){
    vector<Socks> my_products = this->my_controller.get_products();
    vector<Socks> my_cart = this->my_controller.get_cart();
    int operation, size_int;
    string size;
    cout<<"Enter the size of the socks you are looking for: ";
    cin.clear();
    cin.get();
    getline(cin, size);
    try {
        if(size.size() == 0)
            size_int = 0;
        else
            size_int = stoi(size);
        int current_index = 0;
        Socks current_sock = this->my_controller.get_next_sock(my_products, current_index, size_int);
        while (true) {
            if(current_sock.get_colour().size()==0){
                cout<<"There are no socks of the given size.\n\n";
                break;
            }
            cout<<"\n";
            this->print_sock(current_sock);
            cout<<"1. Move to the next sock.\n2. Add to shopping cart.\n3. Go back.\n";
            cout<<"Give operation: ";
            cin>>operation;
            if(cin.fail()){
                cout<<"You did not enter an integer.\n\n";
                cin.clear();
                cin.ignore();
            } else {
                if (operation == 1) {
                    current_sock = this->my_controller.get_next_sock(my_products, current_index, size_int);
                } else if (operation == 2) {
                    this->my_controller.add_to_cart(my_products, my_cart, current_sock);
                } else if (operation == 3) {
                    return;
                }
            }

        }

    }
    catch (exception) {
        cout<<"You did not enter a number or an emtpy sting. Program terminating.\n\n";
        return;
    }
}

void Console::print_user_menu(){
    cout<<"1. See all socks available, given a certain size (leave empty for all socks).\n";
    cout<<"2. View shopping basket.\n";
    cout<<"3. Save shopping basket to file.\n";
    cout<<"4. Open shopping basket.\n";
    cout<<"5. Go one layer up in the application.\n";
}

void Console::display_shopping_cart(){
    if(this->my_controller.get_cart_length() == 0){
        cout<<"No socks here bruh.\n\n";
        return;
    }
    vector<Socks> my_cart = this->my_controller.get_cart();
    int total_sum = 0;
    for(Socks& current_sock:my_cart) {
        cout<<"Socks number " << &current_sock - &my_cart[0] + 1<<endl;
        this->print_sock(current_sock);
        total_sum+=current_sock.get_quantity()*current_sock.get_price();
    }
    cout<<"The total amount of money to pay is: "<<total_sum<<endl<<endl;

}

void Console::run_user(){
    int option;
    bool running = true;
    while (running) {
        this->print_user_menu();
        cout<<"Please enter the option: ";
        cin>>option;
        if(cin.fail()){
            cout<<"You did not enter an integer.\n\n";
            cin.clear();
            cin.ignore();
        } else {
            if(option == 1)
                this->go_through_shop();
            else if (option == 2)
                this->display_shopping_cart();
            else if (option == 5)
                return;
            else if (option == 3)
                this->my_controller.save_shopping_cart();
            else if (option == 4)
                this->my_controller.open_shopping_cart();
            else
                cout<<"Option not available.\n\n";
        }

    }
}


void Console::run(){
    int option;
    bool running = true;
    while (running){
        cout<<"Press 1 for administrator, 2 for user, 3 to exit the app: ";
        cin>>option;
        if(cin.fail()){
            cout<<"You did not enter an integer.\n\n";
            cin.clear();
            cin.ignore();
        } else {
            if(option == 1)
                this->run_administrator();
            else if (option == 2)
                this->run_user();
            else if (option == 3)
                running = false;
            else
                cout<<"Option not available.\n\n";
        }
    }
}
