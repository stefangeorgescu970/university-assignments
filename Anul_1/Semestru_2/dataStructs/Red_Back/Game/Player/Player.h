//
// Created by Georgescu Stefan on 02/06/2017.
//

#ifndef RED_BACK_PLAYER_H
#define RED_BACK_PLAYER_H

#include "../../DataStructures/Queue/Queue.h"


class Player {
    /*
     * Class representing a player of the Red-Back Card Game.
     * We will keep a record of his cards using a Queue.
     */
private:
    Queue my_cards;

public:
    Player(int number_of_cards);
    // Constructor for the Player class.

    std::string play_card();
    // Function used to play a card.

    void take_card(std::string colour);
    // Function used to add a card to his deck.

    bool has_no_cards();
    // Check if a player is out of cards.
};


#endif //RED_BACK_PLAYER_H
