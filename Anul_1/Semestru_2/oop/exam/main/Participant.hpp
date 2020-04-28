//
//  Participant.hpp
//  main
//
//  Created by Georgescu Stefan on 19/06/2017.
//
//

#ifndef Participant_hpp
#define Participant_hpp

#include <stdio.h>
#include <string>

class Participant {
private:
    std::string name;
    int score;
    
public:
    Participant(std::string name);
    
    int getScore();
    
    std::string getName();
    
    void setScore(int score);
};



#endif /* Participant_hpp */
