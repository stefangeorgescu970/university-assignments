//
// Created by Georgescu Stefan on 02/06/2017.
//

#ifndef RED_BACK_REDBACKEXCEPTION_H
#define RED_BACK_REDBACKEXCEPTION_H

#include <exception>

class RedBackException : public std::exception {
public:
    const char* what () const throw () {
        return "An odd exception occured in our app.\n\n";
    }
};

class StackOverflowException : public  RedBackException {
public:
    const char* what () const throw () {
        return "Stack Overflow!\n\n";
    }
};

class StackUnderflowException : public  RedBackException {
public:
    const char* what () const throw() {
        return "Stack Underflow!\n\n";
    }
};

class QueueOverflowException : public  RedBackException {
public:
    const char* what () const throw () {
        return "Queue Overflow!\n\n";
    }
};

class QueueUnderflowException : public  RedBackException {
public:
    const char* what () const throw() {
        return "Queue Underflow!\n\n";
    }
};

class GameInitException : public RedBackException {
public:
    const char* what () const throw() {
        return "Error when initialising the game!\n\n";
    }
};
#endif //RED_BACK_REDBACKEXCEPTION_H
