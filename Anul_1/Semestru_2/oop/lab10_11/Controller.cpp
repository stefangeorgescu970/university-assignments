//
//  Controller.cpp
//  lab5_6
//
//  Created by Georgescu Stefan on 27/03/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include "Controller.hpp"
#include <string.h>
#include <iostream>
#include "Exceptions.cpp"


/**
 Constructor for the Controller class.
 */



Controller::Controller(Repository* my_repository){
    this->my_repository = my_repository;
}

Controller::Controller(){
}


/**
 Creates a new sock and adds it to the repository.

 @param size the size of the new sock, integer.
 @param price the price of the new sock, integer.
 @param quantity the quantity of the new sock, integer.
 @param colour the colour of the new sock, pointer to char.
 @param photograph the photograph of the new sock, pointer to char.
 @return true if the sock was added and false otherwise.
 */
bool Controller::add(int size, int price, int quantity, string colour, string photograph){
    Socks new_sock(size, price, quantity, colour, photograph);
    int did_find = get_sock_by_identificators(size, colour);
    if (did_find == -1){
        
        this->my_repository->add(new_sock);
        return true;
    }
    throw RepoAddException();
}

/**
 Get a pointer to a sock matching the unique identificator.

 @param size the size of the socks, integer.
 @param colour the colour of the socks, pointer to char.
 @return returns a pointer to the socks if they were found, or NULL otherwise.
 */
int Controller::get_sock_by_identificators(int size, string colour){
    if(this->get_length() == 0)
        return -1;
    vector<Socks> my_products = this->my_repository->get_products();
    for ( Socks& current_sock:my_products )
        if (current_sock.get_size() == size and current_sock.get_colour() == colour)
            return (int)(&current_sock - &my_products[0]);
    return -1;
}

/**
 Remove a sock from the repository.

 @param size the size of the socks, integer.
 @param colour the colour of the socks, pointer to char.
 @return ture if the sock was found and removed, false otherwise.
 */
bool Controller::remove(int size, string colour){
    int did_find = get_sock_by_identificators(size, colour);
    if(did_find != -1){
        this->my_repository->remove(did_find);
        return true;
    }
    throw RepoRemoveException();
}

/**
 Get the length of the repository.

 @return the number of socks stored in memory.
 */
int Controller::get_length(){
    return this->my_repository->get_length();
}

int Controller::get_cart_length(){
    return this->my_repository->get_cart_length();
}

/**
 Updates the quantity of a sock.

 @param size the size of the sock, integer.
 @param colour the colour of the sock, pointer to char.
 @param new_qunatity the new quantity, integer.
 @return true if the sock was found and updated, false otherwise.
 */
bool Controller::update_quantity(int size, string colour, int new_qunatity){
    return this->my_repository->update_quantity(size, colour, new_qunatity);
}

/**
 Updates the price of a sock.
 
 @param size the size of the sock, integer.
 @param colour the colour of the sock, pointer to char.
 @param new_price the new price, integer.
 @return true if the sock was found and updated, false otherwise.
 */
bool Controller::update_price(int size, string colour, int new_price){
    return this->my_repository->update_price(size, colour, new_price);
}


void Controller::add_to_cart(vector<Socks>& my_products, vector<Socks>& my_cart, Socks& socks){
    if (socks.get_quantity() == 0){
        throw AddToCartException();
    }
    int number_of_items = (int)my_cart.size();
    for (int index = 0; index < number_of_items; index++) {
        if (my_cart[index].get_size() == socks.get_size() and my_cart[index].get_colour() == socks.get_colour()) {
            my_cart[index].set_quantity(my_cart[index].get_quantity() + 1);
            int index_to_decrease = this->get_sock_by_identificators(socks.get_size(), socks.get_colour());
            my_products[index_to_decrease].set_quantity(my_products[index_to_decrease].get_quantity() - 1);
            socks.set_quantity(socks.get_quantity() - 1);
            set_cart(my_cart);
            set_products(my_products);
            return;
        }
    }
    Socks new_sock(socks.get_size(), socks.get_price(), 1, socks.get_colour(), socks.get_photograph());
    my_cart.push_back(new_sock);
    socks.set_quantity(socks.get_quantity() - 1);
    int index_to_decrease = this->get_sock_by_identificators(socks.get_size(), socks.get_colour());
    my_products[index_to_decrease].set_quantity(my_products[index_to_decrease].get_quantity() - 1);

    set_cart(my_cart);
    set_products(my_products);
    
}

Socks Controller::get_next_sock(vector<Socks> my_products, int& current_index, int size){
    int no_of_steps = this->get_length() + 2;
    while (no_of_steps) {
        Socks sock = my_products[current_index];
        if(current_index + 1 == get_length())
            current_index = 0;
        else
            current_index++;
        if(sock.get_size() == size or size == 0)
            return sock;
        no_of_steps--;
    }
    return Socks();
}

vector<Socks> Controller::get_products(){
    return this->my_repository->get_products();
}

vector<Socks> Controller::get_cart(){
    return this->my_repository->get_all_cart();
}

void Controller::set_cart(vector<Socks> my_cart){
    this->my_repository->set_cart(my_cart);
}

void Controller::set_products(vector<Socks> my_products){
    this->my_repository->set_products(my_products);
}

void Controller::save_shopping_cart(){
    this->my_repository->save_basket_to_file();
}

void Controller::open_shopping_cart(){
    this->my_repository->show_basket_from_file();
}

vector<Socks> Controller::filter_by_size(string size){
    vector<Socks> my_filtered_socks;
    int size_int = stoi(size);
    for(auto sock: this->get_products())
        if (sock.get_size() == size_int)
            my_filtered_socks.push_back(sock);
    return my_filtered_socks;
}


