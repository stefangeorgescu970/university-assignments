//
// Created by Georgescu Stefan on 02/06/2017.
//

#ifndef RED_BACK_QUEUE_H
#define RED_BACK_QUEUE_H
#include <string>


typedef struct QueueNode{
    /*
     * Structure used to keep all the info required for a Node in a Doubly Linked List on an Array.
     * Colour of a card as a string.
     * The next and previous nodes as integers.
     */
    std::string colour;
    int previous;
    int next;
}QueueNode;


class Queue {
    /*
     * Class representing a Queue implemented on a doubly linked list on an array.
     * We have an array of QueueNodes with static allocation.
     * The capacity, the current size, the head, the tail and the first empty spot as integers.
     * Note: Since we use no dynamic allocation, we do not need a constructor.
     *       We will use the Queue to store cards of different colours.
     */

private:
    QueueNode nodes[200];
    int capacity;
    int size;
    int head;
    int tail;
    int first_empty;

    int allocate();
    // Function used to prepare a spot in the array for a new node.

    void free(int position);
    // Function used to free up a spot in the array for later use.

public:
    Queue(int capacity);
    // Constructor for Data Type Queue.

    void push(std::string colour);
    // Function for pushing a new element in the queue.

    std::string pop();
    // Function for popping an element from the queue.

    std::string top();
    // Function for checking the element at the front of the queue.

    bool is_empty();
    // Function for checking if the Queue is empty.

    bool is_full();
    // Function for checking if the Queue is full.
};


#endif //RED_BACK_QUEUE_H
