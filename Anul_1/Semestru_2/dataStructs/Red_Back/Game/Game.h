//
// Created by Georgescu Stefan on 02/06/2017.
//

#ifndef RED_BACK_GAME_H
#define RED_BACK_GAME_H

#include "Player/Player.h"
#include "Table/Table.h"

class Game {
    /*
     * Class representing the Red-Back Card Game.
     * We have two players, data type Player, and a table, data type Table.
     * The number of cards the game is being played with is an integer.
     * The state of the game (finished/unfinished) will be kept in a boolean is_over.
     */
private:
    Player player1, player2;
    Table game_table;
    int number_of_cards;
    int current_player;
    bool is_over;

    void split_cards();
    // Function used to split the cards between the two players.

    void change_player();
    // Function used to change the player.

    std::string play_card(Player* player);
    //Function used to play a card by a player received as a parameter.

public:
    Game(int number_of_cards);
    // Constructor for the Game class.

    std::string play_next_turn();
    // Function used to play the game.

    std::string get_current_player();
    // Get the current player as a string.

    std::string get_other_player();
    // Get the other player as a string.

    bool get_is_over() const;
    // Get the value of the is_over variable.

    void set_is_over(bool is_over);
    // Set the value of the is_over variable.

    void print_cards();
};

#endif //RED_BACK_GAME_H
