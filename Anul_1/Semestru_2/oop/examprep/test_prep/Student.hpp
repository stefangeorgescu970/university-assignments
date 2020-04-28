//
//  Student.hpp
//  test_prep
//
//  Created by Georgescu Stefan on 18/06/2017.
//
//

#ifndef Student_hpp
#define Student_hpp

#include <stdio.h>
#include <string>

class Student {
private:
    int id;
    std::string name;
    int group;
    double grade;
    std::string nameOfGradingTeacher;
    
public:
    Student(int id, std::string name, int group, double grade = 1, std::string nameOfGradingTeacher = "");
    
    int getGroup();
    
    std::string getName();
    
    double getGrade();
    
    bool operator==(const Student& rhs);
};




#endif /* Student_hpp */
