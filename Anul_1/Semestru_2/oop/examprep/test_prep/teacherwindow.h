#ifndef TEACHERWINDOW_H
#define TEACHERWINDOW_H

#include <QMainWindow>
#include "Student.hpp"
namespace Ui {
class TeacherWindow;
}

class TeacherWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit TeacherWindow(QWidget *parent = 0);
    ~TeacherWindow();

    void setAdmittedGroups(std::vector<int> admittedGroups);
    
    void populateStudents(std::vector<Student>);
    
private:
    Ui::TeacherWindow *ui;
    std::vector<int> admittedGroups;
};

#endif // TEACHERWINDOW_H
