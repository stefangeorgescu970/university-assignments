//
//  Repository.cpp
//  main
//
//  Created by Georgescu Stefan on 19/06/2017.
//
//

#include "Repository.hpp"
#include <fstream>
#include <iostream>

using namespace std;

Repository::Repository(string participantFile, string quetionFile){
    this->questionFile = questionFile;
    this->initQuestionData(quetionFile);
    this->initParticipantData(participantFile);
}


void Repository::initParticipantData(std::string fileName){
    ifstream fin (fileName);
    string name;
    while (fin>>name) {
        Participant newParticipant{name};
        this->myParticipants.push_back(newParticipant);
    }
    fin.close();
}

void Repository::initQuestionData(std::string fileName) {
    ifstream fin (fileName);
    Question prevQ;
    string id;
    string text;
    string answer;
    string score;
    while(fin){
        getline(fin, id);
        getline(fin, text);
        getline(fin, answer);
        getline(fin, score);
        Question newQuestion {stoi(id), text, answer, stoi(score)};
        if(newQuestion.getText()!= prevQ.getText())
            this->myQuestions.push_back(newQuestion);
        prevQ = newQuestion;
    }
    fin.close();
}

vector<Question> Repository::getQuestions(){
    return this->myQuestions;
}

vector<Participant> Repository::getParticipants(){
    return this->myParticipants;
}

void Repository::addQuestion(Question &question){
    this->myQuestions.push_back(question);
    this->updateFile();
}

void Repository::updateFile(){
    ofstream f("n.txt");
    for(auto question : this->getQuestions()){
        f<<question.getID()<<"\n"<<question.getText()<<"\n"<<question.getAnswer()<<"\n"<<question.getScore()<<"\n";
    }
    f.close();
    system("rm Questions.txt; mv n.txt Questions.txt");
}

