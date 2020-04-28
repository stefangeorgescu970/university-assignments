//
// Created by Georgescu Stefan on 02/06/2017.
//

#include <cstdlib>
#include "Stack.h"
#include "../../Exceptions/RedBackException.h"

using namespace std;

Stack::Stack(int capacity) {
    /*
     * Creates an empty stack.
     * Prerequisites: Capacity is an integer.
     * Post: This is an empty stack with a maximum capacity specified by the parameter.
     */
    this->capacity = capacity;
    this->size = 0;
    this->head = NULL;
}

Stack::~Stack(){
    /*
     * Destroys a stack
     * Prerequisites: None.
     * Post: This stack was destroyed.
     */
    while(this->head != NULL){
        StackNode* to_delete = this->head;
        this->head = to_delete->next;
        free(to_delete);
    }
}

void Stack::push(string colour) {
    /*
     * Adds a new element in the stack, while respecting the LIFO behaviour of the data type.
     * Prerequisites: The colour of the card is given as a string, and this is not a full Stack.
     * Post: The card will be added on the top of the stack.
     * Throws: StackOverflowException if this is a full Stack.
     */
    if(this->size == this->capacity)
        throw StackOverflowException();

    StackNode* new_card = new StackNode;
    new_card->colour = colour;
    new_card->next = this->head;
    this->head = new_card;
    this->size++;
}

string Stack::pop() {
    /*
     * Eliminates the element on the top of the stack and returns the colour to the caller.
     * Prerequisites: This Stack is not empty.
     * Post: The element was removed from the stack.
     * Returns: The colour of the removed card as a string.
     * Throws: StackUnderflowException if this is an empty Stack.
     */
    if(this->size == 0)
        throw StackUnderflowException();

    StackNode* popped_node = this->head;
    this->head = popped_node->next;
    string card_color = popped_node->colour;
    free(popped_node);
    this->size--;
    return card_color;
}

string Stack::top() {
    /*
     * Used to find the color of the card from the top of the Stack.
     * Prerequisites: This Stack is not empty.
     * Post: No changes are done to the Stack.
     * Returns: The color of the card from the first position in the Stack.
     * Throws: StackUnderflowException if this Stack is empty.
     */
    if(this->size == 0)
        throw StackUnderflowException();

    return this->head->colour;
}

bool Stack::is_empty() {
    /*
     * Check if a stack is empty.
     * Prerequisites: None.
     * Post: No changes are done to the Stack.
     * Returns: True if the stack is empty, False otherwise.
     */
    return this->size == 0;
}

bool Stack::is_full() {
    /*
     * Check if a stack is full.
     * Prerequisites: None.
     * Post: No changes are done to the Stack.
     * Returns: True if the stack is full, False otherwise.
     */
    return this->size == this->capacity;
}



