//
//  Exceptions.cpp
//  lab8_9
//
//  Created by Georgescu Stefan on 20/04/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include <stdio.h>
#include <exception>
using namespace std;

class RepositoryException : public exception {
public:  
const char * what () const throw () {
        return "An odd exception occured in the repository.\n\n";
    }
};

class RepoAddException : public RepositoryException {
public: 
    const char * what () const throw () {
        return "Duplicate product. Not added.\n\n";
    }
};

class RepoRemoveException : public RepositoryException {
public:
    const char * what () const throw () {
        return "Product not found. Remove failed.\n\n";
    }
};

class RepoUpdateException : public RepositoryException {
public: const char * what () const throw () {
    return "Product not found. Update failed.\n\n";
    }
};

class RepoValidateException : public RepositoryException {
public: const char * what () const throw () {
        return "Product does not meet requirements. Who sells socks and gives money to the buyer?.\n\n";
    }
};


class AddToCartException : public RepositoryException {
public: const char * what () const throw () {
        return "No more socks of this type left.\n\n";
    }
};

