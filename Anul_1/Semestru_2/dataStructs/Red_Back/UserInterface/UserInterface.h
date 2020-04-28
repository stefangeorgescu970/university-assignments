//
// Created by Georgescu Stefan on 09/06/2017.
//

#ifndef RED_BACK_USERINTERFACE_H
#define RED_BACK_USERINTERFACE_H


#include "../Game/Game.h"

class UserInterface {
    /*
     * Class used for the user interface.
     * It holds the Game Data Type.
     */
private:
    Game my_game;

    void play_next_turn();
    // Function used to play the next turn of the game.

public:
    UserInterface();
    // Constructor for the class.

    void run();
    // Function used to start the app.
};


#endif //RED_BACK_USERINTERFACE_H
