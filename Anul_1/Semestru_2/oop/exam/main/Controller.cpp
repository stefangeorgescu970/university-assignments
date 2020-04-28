//
//  Controller.cpp
//  main
//
//  Created by Georgescu Stefan on 19/06/2017.
//
//

#include "Controller.hpp"
#include <assert.h>

using namespace std;

Controller::Controller(Repository& myRepository) : myRepository{myRepository}{
    this->testAdd();
}

vector<Question> Controller::getQuestions() {
    return this->myRepository.getQuestions();
}

vector<Participant> Controller::getParticipants(){
    return this->myRepository.getParticipants();
}


bool Controller::addQuestion(int id, std::string text, std::string answer, int score){
    /*
     Add a question.
     Pre: id is int and unique, text is string and not emptu, answer is string, score is int.
     Will check if the id is unique and that the text is not empty. Will not modify the repo if those two conditions are not met.
     Returns: true if the question was added, false otherwise. 
     */
    for(auto q : this->myRepository.getQuestions())
        if(id == q.getID())
            return false;
    if(text.size() == 0)
        return false;
    Question newQuestion{id, text, answer,score};
    this->myRepository.addQuestion(newQuestion);
    return true;
}


void Controller::testAdd(){
    assert(this->addQuestion(1, "cv", "cv", 0) == false);
    assert(this->addQuestion(5, "", "cv", 0) == false);
    assert(this->addQuestion(5, "Test q?", "Yes", 20));
}
