#include "teacherwindow.h"
#include "ui_teacherwindow.h"
using namespace std;

TeacherWindow::TeacherWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::TeacherWindow)
{
    ui->setupUi(this);
}

TeacherWindow::~TeacherWindow()
{
    delete ui;
}

void TeacherWindow::setAdmittedGroups(std::vector<int> admittedGroups){
    this->admittedGroups = admittedGroups;
}

void TeacherWindow::populateStudents(vector<Student> myStudents){
    this->ui->populateList(myStudents, this->admittedGroups);
}
