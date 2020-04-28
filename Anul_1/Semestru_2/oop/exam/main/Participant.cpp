//
//  Participant.cpp
//  main
//
//  Created by Georgescu Stefan on 19/06/2017.
//
//

#include "Participant.hpp"
using namespace std;

Participant::Participant(string name){
    this->name = name;
    this->score = 0;
}

int Participant::getScore(){
    return this->score;
}

string Participant::getName(){
    return this->name;
}

void Participant::setScore(int score){
    this->score = score;
}
