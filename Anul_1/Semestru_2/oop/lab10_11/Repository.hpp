//
//  Repository.hpp
//  lab5_6
//
//  Created by Georgescu Stefan on 27/03/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#pragma once
#include <vector>
#include "Socks.hpp"

class Repository{
private:
    vector<Socks> my_products;
    vector<Socks> my_shopping_cart;
    SocksValidator my_validator;
    string file_name;
    
public:
    Repository(string file_name);
    // Constructor for the Repository class.
    
    void add(Socks& new_socks);
    // Add a new sock to the repository.
    
    void remove(int index);
    // Remove a sock from the repository.
    
    int get_length();
    // Getter for the length property of the DynamicVector.
    
    int get_cart_length();
    
    void add_to_cart(Socks& new_socks);
    
    bool update_quantity(int size, string colour, int new_quantity);
    
    bool update_price(int size, string colour, int new_price);
    
    vector<Socks> get_all_cart();
    
    vector<Socks> get_products();
    
    void set_cart(vector<Socks> my_cart);
    
    void set_products(vector<Socks> my_products);
    
    void save_to_file();
    
    void load_from_file();
    
    virtual void save_basket_to_file() = 0;
    
    virtual void show_basket_from_file() = 0;
};

class RepositoryCSV : public Repository{
private:
    string basket_file_name;
public:
    RepositoryCSV(string basket_file_name, string file_name);
    
    void save_basket_to_file() override;
    
    void show_basket_from_file() override;
};

class RepositoryHTML : public Repository{
private:
    string basket_file_name;
public:
    RepositoryHTML(string basket_file_name, string file_name);
    
    void save_basket_to_file() override;
    
    void show_basket_from_file() override;
};














