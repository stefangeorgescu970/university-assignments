//
//  Socks.hpp
//  lab5_6
//
//  Created by Georgescu Stefan on 22/03/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//
#pragma once
#include <string>
#include <iostream>
using namespace std;

class Socks {
private:
    int size, price, quantity;
    string colour, photograph;
public:
    Socks();
    
    Socks(int size, int price, int quantity, string colour, string photograph);
    // Constructor for the Socks class.
    
    bool operator==(const Socks& sock2);
    // Operator overloading for the == operator.
    
    friend istream& operator>>(istream &cin, Socks& sock);
    
    friend ostream& operator<<(ostream &cout, Socks& sock);
    
    
    int get_size() const;
    // Getter for the size attribute.
    
    int get_price();
    // Getter for the price attribute.
    
    int get_quantity();
    // Getter for the quantity attribute.
    
    string get_colour() const; 
    // Getter for the colour attribute.
    
    string get_photograph();
    // Getter for the photograph attribute.
    
    void set_price(int new_price);
    // Setter for the price attribute.
    
    void set_quantity(int new_quantity);
    // Setter for the quantity attribute.
    
    ~Socks();
    // Deconstructor for the class Socks.

};

class SocksValidator {
public:
    bool validate_socks(Socks sock);
};
