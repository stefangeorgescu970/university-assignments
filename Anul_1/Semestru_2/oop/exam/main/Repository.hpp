//
//  Repository.hpp
//  main
//
//  Created by Georgescu Stefan on 19/06/2017.
//
//

#ifndef Repository_hpp
#define Repository_hpp

#include <stdio.h>
#include <vector>
#include "Question.hpp"
#include "Participant.hpp"

class Repository{
    
private:
    std::vector<Question> myQuestions;
    std::vector<Participant> myParticipants;
    
    void initQuestionData(std::string fileName);
    void initParticipantData(std::string fileName);
    
    std::string questionFile;
    
public:
    Repository(std::string participantFile, std::string questionFile);
    
    std::vector<Question> getQuestions();
    
    std::vector<Participant> getParticipants();
    
    void addQuestion(Question& question);
    
    void updateFile();
};

#endif /* Repository_hpp */
