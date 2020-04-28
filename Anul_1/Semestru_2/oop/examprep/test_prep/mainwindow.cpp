#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "dialog.h"
#include <QMessageBox>
#include <QDebug>

using namespace std;


MainWindow::MainWindow(GradeController& myController, QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow),
    myController{}
{
    ui->setupUi(this);
    this->myController = myController;
    this->startTeacherWindows();
    this->populateAllWindows();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::startTeacherWindows(){
    
    vector<Teacher> myTeachers = this->myController.getMyTeachers();
    for( auto teacher : myTeachers){
        TeacherWindow* newWindow = new TeacherWindow{};
        newWindow->setWindowTitle(QString::fromStdString(teacher.getName()));
        newWindow->setAdmittedGroups(teacher.getGroups());
        this->myTeacherWindows.push_back(newWindow);
        newWindow->show();
    }
}

void MainWindow::on_deleteButton_clicked(){
    Student toDelete = this->ui->getSelectedStudent();
    
    bool decision = false;
    
    QMessageBox::StandardButton reply;
    reply = QMessageBox::question(this, "Enquiry", "Do you want to delete that student?",
                                  QMessageBox::Yes|QMessageBox::No);
    if (reply == QMessageBox::Yes) {
        decision = true;
    } else {
        decision = false;
    }
    
    if(decision){
        this->myController.deleteStudent(toDelete);
        this->populateAllWindows();
    }
}


void MainWindow::populateAllWindows(){
    this->ui->populateList(this->myController.getMyStudents());
    for(auto window : myTeacherWindows){
        window->populateStudents(this->myController.getMyStudents());
    }
}


void MainWindow::on_addButton_clicked()
{
    string name = ui->getAddStudentName();
    int group = ui->getAddStudentGroup();
    this->myController.addStudent(name, group);
    this->populateAllWindows();
}
