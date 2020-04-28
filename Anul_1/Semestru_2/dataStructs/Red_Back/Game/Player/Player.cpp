//
// Created by Georgescu Stefan on 02/06/2017.
//

#include "Player.h"

Player::Player(int number_of_cards) : my_cards{number_of_cards} {
    /*
     * Create a player that can hold a maximum number of cards.
     * Prerequisites: The number of cards is given as an integer.
     * Post: Creates a player that currently holds no cards.
     */
}

std::string Player::play_card() {
    /*
     * Play the card on the top of the deck of the player.
     * Prerequisites: The player's hand is not empty.
     * Post: The card is removed from the hand of the player.
     * Returns: The color of the card played by the player.
     * Throws: QueueUnderflowException if the player's hand was empty.
     */
    return this->my_cards.pop();
}

void Player::take_card(std::string colour) {
    /*
     * Take a card and add it to the bottom of the player's deck.
     * Prerequisites: The player's hand is not full.
     * Post: The card is added to the hand of the player.
     * Throws: QueueOverflowException if the player's hand was full.
     */
    this->my_cards.push(colour);
}

bool Player::has_no_cards() {
    /*
     * Check if a player has cards in his hand.
     * Prerequisites: None.
     * Returns: True if the player's hand is empty, False otherwise.
     */
    return this->my_cards.is_empty();
}
