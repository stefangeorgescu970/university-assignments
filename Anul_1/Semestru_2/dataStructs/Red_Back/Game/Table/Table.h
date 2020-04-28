//
// Created by Georgescu Stefan on 02/06/2017.
//

#ifndef RED_BACK_TABLE_H
#define RED_BACK_TABLE_H
#include "../../DataStructures/Stack/Stack.h"

class Table {
    /*
     * Class representing the table the Red-Back Card Game is being played on.
     * We will keep the cards on the table on a Stack.
     */
private:
    Stack cards_on_table;

public:
    Table(int maximum_number_of_cards);
    // Constructor for the Table class.

    void add_card_to_table(std::string colour);
    // Function used for placing a card on the table.

    std::string take_card_from_table();
    // Function used for taking a card from the table.

    bool is_table_empty();
    // Function used to check if the table is empty.
};


#endif //RED_BACK_TABLE_H
