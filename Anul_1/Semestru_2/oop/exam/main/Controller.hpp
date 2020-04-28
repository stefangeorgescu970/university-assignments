//
//  Controller.hpp
//  main
//
//  Created by Georgescu Stefan on 19/06/2017.
//
//

#ifndef Controller_hpp
#define Controller_hpp

#include <stdio.h>
#include "Repository.hpp"

class Controller {
    
private:
    Repository myRepository;
    
public:
    Controller(Repository& myRepository);
    
    std::vector<Question> getQuestions();
    
    std::vector<Participant> getParticipants();
    
    bool addQuestion(int id, std::string text, std::string answer, int score);
    
    
    void testAdd();
};

#endif /* Controller_hpp */
