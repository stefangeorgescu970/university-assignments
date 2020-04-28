//
//  Question.cpp
//  main
//
//  Created by Georgescu Stefan on 19/06/2017.
//
//

#include "Question.hpp"
#include <sstream>

using namespace std;

Question::Question(int id, string text, string correctAnswer, int score){
    this->id = id;
    this->text = text;
    this->correctAnswer = correctAnswer;
    this->score = score;
}

Question::Question(){}

int Question::getScore(){
    return this->score;
}

string Question::getText(){
    return this->text;
}

string Question::getAnswer(){
    return this->correctAnswer;
}

string Question::toStringPresenter(){
    std::ostringstream string;
    string<<this->id<<" "<<this->text<<" "<<this->correctAnswer;
    return string.str();
}

string Question::toStringParticipant(){
    std::ostringstream string;
    string<<this->id<<" "<<this->text<<" "<<this->score;
    return string.str();
}

int Question::getID(){
    return this->id;
}
