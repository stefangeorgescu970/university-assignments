//
//  main.cpp
//  test_try
//
//  Created by Georgescu Stefan on 17/06/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

class Beverage {
private:
    string description;
    
public:
    
    Beverage(string description) {
        this->description = description;
    }
    
    virtual double price() = 0;
    
    virtual void print() { cout<<description;}
    

};



class Coffee: public Beverage {
public:
    Coffee(): Beverage{"Coffee"}{}
    
    double price() override { return 2.5; }
    

};



class Tea : public Beverage {
public:
    Tea () : Beverage{"Tea"} {}
    
    double price() override { return 1.5;}
    

};


class BeverageWithMilk : public Beverage {
private:
    int milkCount;
    Beverage* prev_bev;
    
public:
    BeverageWithMilk(Beverage* beverage, int milkCount) : Beverage{*beverage} {
        this->milkCount = milkCount;
        this->prev_bev = beverage;
    }
    
    double price() override  {
        return this->prev_bev->price() + milkCount*0.5;
    }
    
    void print() override {
        this->prev_bev->print();
        if (milkCount == 0) {
            cout<<", with no milk\n";
        } else {
            cout<<", "<<milkCount<< " added\n";
        }
    }
    

};


class BeverageMachine{
public:
    void prepare(string type, int milkCount){
        Beverage* base_bev;
        if(type == "Coffee")
            base_bev = new Coffee{};
        else
            base_bev = new Tea{};
        Beverage* my_bev = new BeverageWithMilk{base_bev, milkCount};
        my_bev->print();
        delete my_bev;
        delete base_bev;
    }
};

int main() {
    BeverageMachine my_machine;
    my_machine.prepare("Tea", 0);
    my_machine.prepare("Coffee", 1);
    my_machine.prepare("Coffee", 2);
    
    return 0;
}
