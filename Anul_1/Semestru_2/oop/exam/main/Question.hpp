//
//  Question.hpp
//  main
//
//  Created by Georgescu Stefan on 19/06/2017.
//
//

#ifndef Question_hpp
#define Question_hpp

#include <stdio.h>

#include <string>

class Question {
private:
    int id;
    std::string text;
    std::string correctAnswer;
    int score;
    
public:
    Question(int id, std::string text, std::string correctAnswer, int score);
    
    Question();
    
    int getScore();
    
    int getID();
    
    std::string getText();
    
    std::string getAnswer();
    
    std::string toStringPresenter();
    
    std::string toStringParticipant();
};


#endif /* Question_hpp */
