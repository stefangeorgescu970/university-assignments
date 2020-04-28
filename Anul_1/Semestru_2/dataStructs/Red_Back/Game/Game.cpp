//
// Created by Georgescu Stefan on 02/06/2017.
//

#include "Game.h"
#include "../Exceptions/RedBackException.h"
#include <vector>
#include <iostream>
#include <random>

using namespace std;

Game::Game(int number_of_cards) : player1{number_of_cards}, player2{number_of_cards}, game_table{number_of_cards}{
    /*
     * Constructor for the Game class.
     * Prerequisites: The number of cards is given as an even positive integer.
     * Post: Creates a game where both players have their cards, and an empty table.
     * Throws: GameInitException if the preconditions are not met.
     */
    if (number_of_cards <= 0 or number_of_cards % 2 != 0 or number_of_cards > 200)
        throw GameInitException();
    this->number_of_cards = number_of_cards;
    this->is_over = false;
    this->split_cards();
    this->current_player = 1;
}

void Game::split_cards() {
    /*
     * Split a deck of cards between the two players.
     * Prerequisites: None.
     * Post: Both players will receive half of the deck.
     */
    vector<string> deck;
    for(int index = 1; index <= this->number_of_cards; index++)
        if(index > number_of_cards/2)
            deck.push_back("Red");
        else
            deck.push_back("Black");

    random_device rd;
    mt19937 mt(rd());
    uniform_real_distribution<double> dist(1, 11);

    double number_of_shuffles = dist(mt);
    for(int shuffle_count = 0; shuffle_count < number_of_shuffles; shuffle_count++)
        shuffle(deck.begin(), deck.end(), default_random_engine());

    for(int index = 0; index < this->number_of_cards; index++){
        this->player1.take_card(deck[index]);
        this->player2.take_card(deck[++index]);
    }

}


void Game::print_cards() {
    cout<<"Player 1 cards: \n";
    for(int index = 0; index < this->number_of_cards / 2; index++){
        string card = this->player1.play_card();
        cout<<card<<"\n";
        this->player1.take_card(card);
    }
    cout<<"\n";
    cout<<"Player 2 cards: \n";
    for(int index = 0; index < this->number_of_cards / 2; index++){
        string card = this->player2.play_card();
        cout<<card<<"\n";
        this->player2.take_card(card);
    }
    cout<<"\n";
}

string Game::play_next_turn() {
    /*
     * Simulation of a turn in the game.
     * Prerequisites: None.
     * Post: Exchanges cards between players accordingly.
     * Returns: The color of the card played, or an empty string if the player does not have a card to play.
     */

    Player* player, *other_player;

    (current_player == 1) ? player = &this->player1 : player = &this->player2;
    (current_player == 1) ? other_player = &this->player2 : other_player = &this->player1;

    if (player->has_no_cards())
        return "";

    string played_card = this->play_card(player);

    if (played_card == "Red") {
        while (!this->game_table.is_table_empty()) {
            other_player->take_card(this->game_table.take_card_from_table());
        }
    }

    this->change_player();
    return played_card;
}

void Game::change_player() {
    /*
     * Changes the current player.
     * Prerequisites: None.
     * Post: Changes the current player to the other player.
     */
    (this->current_player == 1) ? this->current_player = 2 : this->current_player = 1;
}


string Game::play_card(Player* player) {
    /*
     * A player puts a card on the table.
     * Prerequisites: player is a pointer to type Player.
     * Post: Player has put his first card on the table.
     * Returns: The color of the card played, as a string.
     */
    string player_card = player->play_card();
    this->game_table.add_card_to_table(player_card);
    return player_card;
}

std::string Game::get_current_player() {
    /*
     * Gets the current player.
     * Prerequisites: None.
     * Post: Nothing is changed.
     * Returns: A string of form Player 1 or Player 2.
     */
    if (this->current_player == 1)
        return "Player 1";
    return "Player 2";
}

std::string Game::get_other_player() {
    /*
     * Gets the current player.
     * Prerequisites: None.
     * Post: Nothing is changed.
     * Returns: A string of form Player 1 or Player 2.
     */
    if (this->current_player == 2)
        return "Player 2";
    return "Player 1";
}

bool Game::get_is_over() const {
    /*
     * Shows if the game is over.
     * Prerequisites: None.
     * Post: Nothing is changed in memory.
     * Returns: Boolean showing if the game is over or not.
     */
    return this->is_over;
}

void Game::set_is_over(bool is_over) {
    /*
     * Sets if the game is over or not.
     * Prerequisites: is_over is provided as a boolean value.
     * Post: changes this->is_over with the new bool value provided by the arguments.
     */
    this->is_over = is_over;
}
