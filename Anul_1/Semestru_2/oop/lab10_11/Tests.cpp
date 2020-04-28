//
//  Tests.cpp
//  lab8_9
//
//  Created by Georgescu Stefan on 20/04/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include "Tests.hpp"
#include "Socks.hpp"
#include "Repository.hpp"
#include "Controller.hpp"
#include "Exceptions.cpp"
#include <assert.h>

void Tests::test_Socks(){
    Socks my_sock {10, 20, 30, "Red", "Link"};
    assert(my_sock.get_size() == 10);
    assert(my_sock.get_price() == 20);
    assert(my_sock.get_quantity() == 30);
    assert(my_sock.get_colour() == "Red");
    assert(my_sock.get_photograph() == "Link");
    my_sock.set_price(40);
    assert(my_sock.get_price() == 40);
    my_sock.set_quantity(50);
    assert(my_sock.get_quantity() == 50);
    Socks my_other_sock {10, 20, 30, "Red", "Link"};
    assert(my_sock == my_other_sock);
    Socks some_other_sock {10, 20, 30, "Green", "Link"};
    assert(!(my_other_sock == some_other_sock));
}

void Tests::test_Repository(){
    RepositoryCSV my_repo {"dummy", "/Users/Stefan/Documents/Facultate/Anul_1/Semestru_2/Object_Oriented_Programming/lab10_11/socks_test.txt"};
    vector<Socks> copy = my_repo.get_products();
    assert(my_repo.get_length() == 3);
    assert(my_repo.get_cart_length() == 0);
    Socks my_sock {10, 20, 30, "Red", "Link"};
    Socks my_other_sock {10, 20, 30, "Red", "Link"};
    my_repo.add(my_sock);
    assert(my_repo.get_length() == 4);
    Socks some_other_sock {10, -20, 30, "Green", "Link"};
    try{
        my_repo.add(some_other_sock);
        assert(false);
    } catch (RepoValidateException& exc) {
        assert(true);
    }
    assert(my_repo.get_length() == 4);
    my_repo.remove(3);
    assert(my_repo.get_length() == 3);
    my_repo.add_to_cart(my_other_sock);
    assert(my_repo.get_cart_length() == 1);
    my_repo.add(my_sock);
    my_repo.update_quantity(10, "Red", 50);
    assert(my_repo.get_products()[3].get_quantity() == 50);
    my_repo.update_price(10, "Red", 60);
    assert(my_repo.get_products()[3].get_price() == 60);
    vector<Socks> my_vector;
    my_vector.push_back(my_sock);
    my_vector.push_back(my_other_sock);
//    assert(my_repo.get_products() != my_vector);
//    assert(my_repo.get_all_cart() != my_vector);
    my_repo.set_cart(my_vector);
    my_repo.set_products(my_vector);
//    assert(my_repo.get_products() == my_vector);
//    assert(my_repo.get_all_cart() == my_vector);
    my_repo.set_products(copy);
}

void Tests::test_Controller(){
    RepositoryCSV* my_repo = new RepositoryCSV{"dummy","/Users/Stefan/Documents/Facultate/Anul_1/Semestru_2/Object_Oriented_Programming/lab10_11/socks_test.txt"};
    Controller my_controller{my_repo};
    vector<Socks> copy = my_controller.get_products();
    
    assert(my_controller.add(1, 1, 1, "1", "1"));
    try {
        my_controller.add(1, 1, 1, "1", "1");
        assert(false);
    } catch (RepoAddException& exc) {
        assert(true);
    }
    
    assert(my_controller.remove(1, "1"));
    try {
        my_controller.remove(1, "1");
        assert(false);
    } catch (RepoRemoveException& exc) {
        assert(true);
    }
    
    assert(my_controller.get_length() == 3);
    
    assert(my_controller.add(1, 1, 1, "1", "1"));
    
    assert(my_controller.update_price(1, "1", 10));
    assert(my_controller.update_quantity(1, "1", 10));
    
    try {
        my_controller.update_price(2, "2", 2);
        assert(false);
    } catch (RepoUpdateException& exc) {
        assert(true);
    }
    
    try {
        my_controller.update_quantity(2, "2", 2);
        assert(false);
    } catch (RepoUpdateException& exc) {
        assert(true);
    }
    
    assert(my_controller.remove(1, "1"));
    
    vector<Socks> my_prod = my_controller.get_products();
    vector<Socks> my_cart;
    Socks my_sock = my_prod[0];
    
    my_controller.add_to_cart(my_prod, my_cart, my_sock);
    assert(my_controller.get_cart_length() == 1);
    my_controller.add_to_cart(my_prod, my_cart, my_sock);
    assert(my_controller.get_cart_length() == 1);
    int current = 0;
    assert(my_controller.get_next_sock(my_prod, current, 0) == my_prod[0]);
    
}

void Tests::test_all(){
    test_Socks();
    test_Repository();
    test_Controller();
}
