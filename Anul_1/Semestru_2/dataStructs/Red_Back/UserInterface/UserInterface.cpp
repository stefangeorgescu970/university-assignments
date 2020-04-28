//
// Created by Georgescu Stefan on 09/06/2017.
//

#include <iostream>
#include <unistd.h>
#include "UserInterface.h"
#include "../Exceptions/RedBackException.h"

using namespace std;

UserInterface::UserInterface() : my_game{2} {}

void UserInterface::run() {
    /*
     * Function that plays the game, in turns.
     * Will terminate when one player wins.
     */
    int size_of_deck;
    cout<<"App is starting now.\n\n";
    cout<<"Please enter the size of the deck you are playing with. That should be an even integer by the way: ";
    cin>>size_of_deck;
    try {
        Game my_game{size_of_deck};
        this->my_game = my_game;
        this->my_game.print_cards();
        while(!this->my_game.get_is_over()) {
            //sleep(1);
            this->play_next_turn();
        }
        string winner = this->my_game.get_other_player();
        cout<<winner + " has won.\n";
    } catch (GameInitException& exc) {
        cout<<exc.what();
    }
}

void UserInterface::play_next_turn() {
    /*
     * Function that plays one turn.
     * Prints to the console what happened.
     */
    string player = this->my_game.get_current_player();
    string played_card = this->my_game.play_next_turn();
    string to_print;
    if (played_card == ""){
        this->my_game.set_is_over(true);
    } else if (played_card == "Red") {
        string other_player = this->my_game.get_other_player();
        to_print = player + " has played a red card. " + other_player + " takes all cards.\n";
    } else if (played_card == "Black") {
        to_print = player + " has played a black card.\n";
    }
    cout<<to_print;
}

