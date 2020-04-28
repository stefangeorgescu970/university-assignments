//
//  Teacher.hpp
//  test_prep
//
//  Created by Georgescu Stefan on 18/06/2017.
//
//

#ifndef Teacher_hpp
#define Teacher_hpp

#include <stdio.h>
#include <string>
#include <vector>

class Teacher {
private:
    std::string name;
    std::vector<int> groupsICanGrade;
    
public:
    Teacher(std::string name);
    
    void addGroupICanGrade(int group);
    
    std::string getName();
    
    std::vector<int> getGroups();
};

#endif /* Teacher_hpp */
