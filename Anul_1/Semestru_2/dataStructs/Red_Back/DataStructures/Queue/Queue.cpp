//
// Created by Georgescu Stefan on 02/06/2017.
//

#include "Queue.h"
#include "../../Exceptions/RedBackException.h"
using namespace std;

Queue::Queue(int capacity) {
    /*
     * Creates an empty queue.
     * Prerequisites: Capacity is an integer.
     * Post: This is an empty queue with a maximum capacity specified by the parameter.
     */
    this->capacity = capacity;
    for(int index = 0; index < capacity; index++){
        this->nodes[index].next = index + 1;
        this->nodes[index].previous = -1;
    }
    this->nodes[capacity-1].next = -1;
    this->size = 0;
    this->head = -1;
    this->tail = -1;
    this->first_empty = 0;
}

int Queue::allocate() {
    /*
     * Prepare a spot in the array for a new node. This is to make implementation similar to dynamic allocation.
     * Prerequisites: -
     * Post: At the returned position we will have space prepared for a new element. first_empty, head and tail will
     * change accordingly.
     * Returns: The index at which we insert the following node, or -1 if queue is full.
     */
    int new_element = this->first_empty;
    if (new_element != -1) {
        this->first_empty = this->nodes[this->first_empty].next;
        this->nodes[this->first_empty].previous = -1;
        this->nodes[new_element].next = -1;
        this->nodes[new_element].previous = -1;
    }
    return new_element;
}

void Queue::free(int position) {
    /*
     * Put the position we want to free in the list of empty nodes.
     * Prerequisites: The position is given as an integer.
     * Post: The position specified will be added as the first empty position, so it can be accessed later.
     */
    this->nodes[position].next = this->first_empty;
    this->nodes[position].previous = -1;
    this->nodes[this->first_empty].previous = position;
    this->first_empty = position;
}

void Queue::push(string colour) {
    /*
     * Add a new element in the queue, while respecting the FIFO behaviour of the data type.
     * Prerequisites: The colour of the card is given as a string, and this is not a full Queue.
     * Post: The card will be added at the end of the queue.
     * Throws: QueueOverflowException if this is a full Queue.
     */
    if(this->size == this->capacity)
        throw(QueueOverflowException());

    int new_element = allocate();
    if(this->tail == -1) {
        this->tail = this->head = new_element;
        this->nodes[new_element].colour = colour;
    } else {
        this->nodes[new_element].colour = colour;
        this->nodes[new_element].previous = this->tail;
        this->nodes[this->tail].next = new_element;
        this->tail = new_element;
    }
    this->size++;
}

std::string Queue::pop() {
    /*
     * Eliminates the element at the beginning of the queue and returns the colour to the caller.
     * Prerequisites: This Queue is not empty.
     * Post: The element was removed from the queue.
     * Returns: The colour of the removed card as a string.
     * Throws: QueueUnderflowException if this is an empty Queue.
     */
    if(this->size == 0)
        throw(QueueUnderflowException());

    string card_colour;

    if(this->head == this->tail){
        card_colour = this->nodes[this->head].colour;
        int pos = this->head;
        this->head = this->tail = -1;
        free(pos);
    }else {
        int head_pos = this->head;
        card_colour = this->nodes[head_pos].colour;
        this->head = this->nodes[head_pos].next;
        this->nodes[this->head].previous = -1;
        free(head_pos);
    }
    this->size--;

    return card_colour;
}


std::string Queue::top() {
    /*
     * Used to find the color of the card from the first position in the Queue.
     * Prerequisites: This Queue is not empty.
     * Post: No changes are done to the Queue.
     * Returns: The color of the card from the first position in the Queue.
     * Throws: QueueUnderflowException if this Queue is empty.
     */
    if(this->size == 0)
        throw(QueueUnderflowException());

    return this->nodes[this->head].colour;
}

bool Queue::is_empty() {
    /*
     * Check if a queue is empty.
     * Prerequisites: None.
     * Post: No changes are done to the Queue.
     * Returns: True if the queue is empty, False otherwise.
     */
    return this->size == 0;
}

bool Queue::is_full() {
    /*
     * Check if a queue is full.
     * Prerequisites: None.
     * Post: No changes are done to the Queue.
     * Returns: True if the queue is full, False otherwise.
     */
    return this->size == this->capacity;
}

