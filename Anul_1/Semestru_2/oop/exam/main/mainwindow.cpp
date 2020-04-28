#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "Participant.hpp"
#include <QMessageBox>
using namespace std;

MainWindow::MainWindow(Controller myController ,QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow),
    myController{myController}
{
    ui->setupUi(this);
    this->runParticipantWindows();
    this->populateList(this->myController.getQuestions());
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_addButton_clicked()
{
    int id = this->ui->getAddID();
    string text = this->ui->getAddText();
    string answer = this->ui->getAddAnswer();
    int score = this->ui->getAddScore();
    bool did_add = this->myController.addQuestion(id, text, answer, score);
    if(did_add) {
        //Question addedQuestion{id, text, answer, score};
        this->populateList(this->myController.getQuestions());
        this->populateParticipant(this->myController.getQuestions());
    } else {
        QMessageBox* newBox = new QMessageBox{};
        newBox->setText(QString::fromStdString("CANNOT ADD THAT"));
        newBox->show();
    }
}

void MainWindow::populateList(std::vector<Question> myQuestions){
    this->ui->populateList(myQuestions);
}

void MainWindow::populateParticipant(std::vector<Question> myQuestions){
    for(auto participant : participantWindows){
        participant->populateList(myQuestions);
    }
}


void MainWindow::runParticipantWindows(){
    vector<Participant> myParticipants = this->myController.getParticipants();
    for(auto participant : myParticipants){
        ParticipantWindow* newWindow = new ParticipantWindow{};
        newWindow->setWindowTitle(QString::fromStdString(participant.getName()));
        newWindow->populateList(this->myController.getQuestions());
        newWindow->show();
        this->participantWindows.push_back(newWindow);
    }
    
}

//void MainWindow::updateWindows(Question &question){
//    this->ui->addNewQuestion(question);
//    for(auto item : participantWindows){
//        item->updateWindow(question);
//    }
//}



