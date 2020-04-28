//
// Created by Georgescu Stefan on 02/06/2017.
//

#include "Table.h"

Table::Table(int maximum_number_of_cards) : cards_on_table{maximum_number_of_cards} {
    /*
     * Creates a table with no cards on it and a maximum capacity.
     * Prerequisites: The maximum number of cards is given as an integer.
     * Post: A table with no cards is initialised.
     */
}

void Table::add_card_to_table(std::string colour) {
    /* Add a card to the table.
     * Prerequisites: The card colour is a string, and the table is not full.
     * Post: The card is added to the table.
     * Throws: StackOverflowException if the table was full.
     */
    this->cards_on_table.push(colour);
}

std::string Table::take_card_from_table() {
    /*
     * Take a card from the table.
     * Prerequisites: The table is not empty.
     * Post: The card is taken from the table, and it's colour is given as a string.
     * Returns: The colour of the card taken from the table.
     * Throws: StackUnderflowException if the table was empty.
     */
    return this->cards_on_table.pop();
}

bool Table::is_table_empty() {
    /*
     * Check if the table is empty.
     * Prerequisites: None.
     * Post: No changes are done to the table.
     * Returns: True if the table is empty, False otherwise.
     */
    return this->cards_on_table.is_empty();
}