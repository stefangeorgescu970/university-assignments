//
//  Socks.cpp
//  lab5_6
//
//  Created by Georgescu Stefan on 22/03/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include <string.h>
#include "Socks.hpp"
#include <iostream>

Socks::Socks(){
    this->size = 0;
    this->price = 0;
    this->quantity = 0;
    this->colour = "";
    this->photograph = "";
}

/**
 Constructor for the Socks class.
 @param size - the size of the socks, integer.
 @param price - the price of the socks, integer.
 @param quantity - the quantity available, integer.
 @param colour - the colour of the socks, pointer to char.
 @param photograph - link to the photograph with the socks, poiter to char.
 */

Socks::Socks(int size, int price, int quantity, string colour, string photograph){
    this->size = size;
    this->price = price;
    this->quantity = quantity;
    this->colour = colour;
    this->photograph = photograph;
}

/**
 Getter for the size attribute.

 @return Returns the size of the socks this method gets called on.
 */
int Socks::get_size()const {
    return this->size;
}

/**
 Getter for the price attribute.
 
 @return Returns the price of the socks this method gets called on.
 */
int Socks::get_price(){
    return this->price;
}

/**
 Getter for the quantity attribute.
 
 @return Returns the quantity of the socks this method gets called on.
 */
int Socks::get_quantity(){
    return this->quantity;
}

/**
 Getter for the colour attribute.
 
 @return Returns the colour of the socks this method gets called on.
 */
string Socks::get_colour()const {
    return this->colour;
}

/**
 Getter for the photograph attribute.
 
 @return Returns the photograph of the socks this method gets called on.
 */
string Socks::get_photograph(){
    return this->photograph;
}

/**
 Operator overloading for the == operator.

 @param sock2 The sock the first one will be compared.
 @return Returns one if the socks are equal, 0 otherwise. They are equal if all attributes are equal.
 */
bool Socks::operator==(const Socks& sock2){
    if (this->get_size() != sock2.get_size())
        return false;
    if ( this->get_colour() != sock2.get_colour() )
        return false;
    return true;
}

/**
 Deconstructor for the Socks class.
 */
Socks::~Socks(){
}

/**
 Setter for the price attribute.

 @param new_price the new price of the socks, integer.
 */
void Socks::set_price(int new_price){
    this->price = new_price;
}

/**
 Setter for the quantity attribute.

 @param new_quantity the new quantity of the socks, integer.
 */
void Socks::set_quantity(int new_quantity){
    this->quantity = new_quantity;
}



bool SocksValidator::validate_socks(Socks sock){
    if(sock.get_size() <= 0)
        return false;
    if(sock.get_price() <= 0)
        return false;
    if (sock.get_quantity() <= 0) {
        return false;
    }
    return true;
}



istream& operator>>(istream &cin, Socks& sock){
    cin>>sock.size>>sock.price>>sock.quantity>>sock.colour>>sock.photograph;
    return cin;
}


ostream& operator<<(ostream &cout, Socks& sock) {
    cout<<sock.size<<' '<<sock.price<<' '<<sock.quantity<<' '<<sock.colour<<' '<<sock.photograph<<endl;
    return cout;
    }





