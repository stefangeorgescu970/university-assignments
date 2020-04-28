//
//  GradeRepository.hpp
//  test_prep
//
//  Created by Georgescu Stefan on 18/06/2017.
//
//

#ifndef GradeRepository_hpp
#define GradeRepository_hpp

#include <stdio.h>
#include "Teacher.hpp"
#include "Student.hpp"

class GradeRepository {
private:
    std::vector<Student> myStudents;
    std::vector<Teacher> myTeachers;
    
    void initStudentData(std::string studentFileName);
    
    void initTeacherData(std::string teacherFileName);
    
public:
    GradeRepository(std::string studentFileName, std::string teacherFileName);
    
    GradeRepository();
    
    std::vector<Student> getMyStudents();
    
    std::vector<Teacher> getMyTeacher();
    
    void addStudent(Student new_student);
    
    void deleteStudent(Student student);
};

#endif /* GradeRepository_hpp */
