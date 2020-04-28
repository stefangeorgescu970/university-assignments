//
// Created by Georgescu Stefan on 02/06/2017.
//

#ifndef RED_BACK_STACK_H
#define RED_BACK_STACK_H

#include <string>

typedef struct StackNode{
    /*
     * Structure used to keep all the info required for a node in a Singly Linked List with Dynamic Allocation.
     * Colour of a cards as a string.
     * The address of the next node as a pointer to StackNode.
     */
    std::string colour;
    StackNode* next;
}StackNode;


class Stack {
    /*
     * Class representing a Stack implemented on a singly linked list with dynamic allocation.
     * We have the address of the first element of the list as a pointer to StackNode.
     * The capacity and current size of the stack are given as integers.
     */

private:
    StackNode* head;
    int capacity;
    int size;

public:
    Stack(int capacity);
    // Constructor for Data Type Stack.

    ~Stack();
    // Destructor for Data Type Stack.

    void push(std::string colour);
    // Function for pushing a new element on the stack.

    std::string pop();
    // Function for popping an element from the top of the stack.

    std::string top();
    // Function for checking the element on the top of the stack.

    bool is_empty();
    // Function for checking if the Stack is empty.

    bool is_full();
    // Function for checking if the Stack is full.
};


#endif //RED_BACK_STACK_H
