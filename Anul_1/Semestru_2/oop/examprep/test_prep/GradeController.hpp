//
//  GradeController.hpp
//  test_prep
//
//  Created by Georgescu Stefan on 18/06/2017.
//
//

#ifndef GradeController_hpp
#define GradeController_hpp

#include <stdio.h>
#include "GradeRepository.hpp"

class GradeController{
private:
    GradeRepository myRepository;
    
public:
    GradeController(GradeRepository& myRepository);
    
    GradeController();
    
    std::vector<Student> getMyStudents();
    
    std::vector<Teacher> getMyTeachers();
    
    void addStudent(std::string name, int group);
    
    void deleteStudent(Student student);
};

#endif /* GradeController_hpp */
