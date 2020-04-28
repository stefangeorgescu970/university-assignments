//
//  Repository.cpp
//  lab5_6
//
//  Created by Georgescu Stefan on 27/03/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include "Repository.hpp"
#include <vector>
#include <fstream>
#include "Exceptions.cpp"
#include "Socks.hpp"

void Repository::load_from_file(){
    Socks new_sock{};
    ifstream fin;
    fin.open(this->file_name);
    while (fin>>new_sock) {
        this->my_products.push_back(new_sock);
    }
}

/**
 Constructor with arguments for the Repository.
 */
Repository::Repository(string file_name){
    vector<Socks> my_products, my_shopping_cart;
    this->my_products = my_products;
    this->my_shopping_cart = my_shopping_cart;
    this->file_name = file_name;
    load_from_file();
}


/**
 Add a new sock to the repository.

 @param new_socks pointer to the new sock to be added.
 */
void Repository::add(Socks& new_socks){
    if (!this->my_validator.validate_socks(new_socks))
        throw RepoValidateException();
    this->my_products.push_back(new_socks);
    save_to_file();
}

void Repository::add_to_cart(Socks& new_socks){
    this->my_shopping_cart.push_back(new_socks);
}


/**
 Remove a sock from the repository
 */
void Repository::remove(int index){
    this->my_products.erase(my_products.begin() + index);
    save_to_file();
}

/**
 Getter for the length of the repository.

 @return the number of socks stored.
 */
int Repository::get_length(){
    return (int)this->my_products.size();
}

int Repository::get_cart_length(){
    return (int)this->my_shopping_cart.size();
}

/**
 Getter for an iterator on the dynamic vector.

 @return pointer to the created iterator.
 */

bool Repository::update_quantity(int size, string colour, int new_quantity){
    if(this->my_products.size() == 0)
        return false;
    int repo_size = (int)this->my_products.size();
    for (int index = 0; index < repo_size; index++) {
        if(this->my_products[index].get_size() == size and this->my_products[index].get_colour() == colour){
            this->my_products[index].set_quantity(new_quantity);
            save_to_file();
            return true;
        }
    }
    throw RepoUpdateException();
}


bool Repository::update_price(int size, string colour, int new_price){
    if(this->my_products.size() == 0)
        return false;
    int repo_size = (int)this->my_products.size();
    for (int index = 0; index < repo_size; index++) {
        if(this->my_products[index].get_size() == size and this->my_products[index].get_colour() == colour){
            this->my_products[index].set_price(new_price);
            save_to_file();
            return true;
        }
    }
    throw RepoUpdateException();
}

vector<Socks> Repository::get_all_cart(){
    return this->my_shopping_cart;
}

vector<Socks> Repository::get_products(){
    return this->my_products;
}

void Repository::set_cart(vector<Socks> my_cart){
    this->my_shopping_cart = my_cart;
}

void Repository::set_products(vector<Socks> my_products){
    this->my_products = my_products;
    save_to_file();
}

void Repository::save_to_file(){
    ofstream fout(this->file_name);
    for (Socks& current_sock:my_products){
        fout<<current_sock;
    }
}

RepositoryCSV::RepositoryCSV(string basket_file_name, string file_name) : Repository(file_name){
    this->basket_file_name = basket_file_name;
}

void RepositoryCSV::save_basket_to_file(){
    ofstream fout(this->basket_file_name);
    vector<Socks> my_basket = this->get_all_cart();
    for(Socks& sock:my_basket){
        fout<<sock.get_size()<<","<<sock.get_price()<<","<<sock.get_quantity()<<","<<sock.get_colour()<<","<<sock.get_photograph()<<"\n";
    }
}

void RepositoryCSV::show_basket_from_file(){
    system("open -a TextEdit basket_CSV.csv");
}

RepositoryHTML::RepositoryHTML(string basket_file_name, string file_name) : Repository(file_name){
    this->basket_file_name = basket_file_name;
}

void RepositoryHTML::save_basket_to_file(){
    ofstream fout(this->basket_file_name);
    vector<Socks> my_basket = this->get_all_cart();
    fout<<"<!DOCTYPE htlm>\n";
    fout<<"<html>\n";
    fout<<"<head>\n";
    fout<<"<title>Socks Shopping Cart</title>\n";
    fout<<"</head>\n";
    fout<<"<body>\n";
    fout<<"<table border=""1"">\n";
    fout<<"<tr>\n";
    fout<<"<td>Size</td>\n";
    fout<<"<td>Price</td>\n";
    fout<<"<td>Quantity</td>\n";
    fout<<"<td>Color</td>\n";
    fout<<"<td>Picture link</td>\n";
    fout<<"</tr>\n";
    for(Socks& sock:my_basket){
        fout<<"<tr>\n";
        fout<<"<td>"<<sock.get_size()<<"</td>\n";
        fout<<"<td>"<<sock.get_price()<<"</td>\n";
        fout<<"<td>"<<sock.get_quantity()<<"</td>\n";
        fout<<"<td>"<<sock.get_colour()<<"</td>\n";
        fout<<"<td><a href = """<<sock.get_photograph()<<""">Link</a></td>\n";
        fout<<"</tr>\n";
    }
    fout<<"</table>\n";
    fout<<"</body>\n";
    fout<<"</html>\n";
}

void RepositoryHTML::show_basket_from_file(){
    system("open -a Safari basket_html.html");
}





