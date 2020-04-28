//
//  Controller.hpp
//  lab5_6
//
//  Created by Georgescu Stefan on 27/03/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#pragma once
#include "Repository.hpp"

class Controller{
private:
    Repository* my_repository;
    int get_sock_by_identificators(int size, string colour);
    // Search for a sock based on the unique identificators.
    
    
public:
    Controller(Repository* my_repository);
    
    Controller();
    
    
    bool add(int size, int price, int quantity, string colour, string photograph);
    // Add a new sock.
    
    bool remove(int size, string colour);
    // Delete a sock.
    
    int get_length();
    // Get the length.
    
    int get_cart_length();
    
    bool update_quantity(int size, string colour, int new_qunatity);
    // Returns true if the sock was found and updated, false otherwise.
    
    bool update_price(int size, string colour, int new_price);
    // Returns true if the sock was found and updated, false otherwise.
    
    void add_to_cart(vector<Socks>& my_products, vector<Socks>& my_cart, Socks& socks);
        // Check if already in cart, if yes get plus one quantity, if not add it, and reduce quantity of the sock in the store.
    
    Socks get_next_sock(vector<Socks> my_products,int& current_index, int size);

    vector<Socks> get_products();
    
    vector<Socks> get_cart();
    
    void set_cart(vector<Socks> my_cart);
    
    void set_products(vector<Socks> my_products);
    
    void save_shopping_cart();
    
    void open_shopping_cart();

    vector<Socks> filter_by_size(string size);
};

