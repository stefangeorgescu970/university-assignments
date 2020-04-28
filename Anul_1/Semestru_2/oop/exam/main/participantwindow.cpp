#include "participantwindow.h"
#include <iostream>
#include "ui_participantwindow.h"
using namespace std;

ParticipantWindow::ParticipantWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::ParticipantWindow)
{
    ui->setupUi(this);
}

ParticipantWindow::~ParticipantWindow()
{
    delete ui;
}

void ParticipantWindow::on_questionList_itemSelectionChanged()
{
    Question selected = this->ui->getSelectedQuestion();
    if(::find(answeredID.begin(), answeredID.end(), selected.getID()) != answeredID.end()) {
        this->ui->invalidateButton();
    } else {
        this->ui->validateButton();
    }
}


void ParticipantWindow::on_pushButton_clicked()
{
    /*
     Function that gives score to a player when answering questions.
     Will get callled when the answer button is pressed.
     Gets the question he should answer, and his answer.
     Pre: player did not answer that question.
     Post: adds score if necessary and colors the question in green.
            The function will not be called if the question was already answered.
     */
    Question wantToAnswer = this->ui->getSelectedQuestion();
    string answer = this->ui->getAnswer();
    
    if(::find(answeredID.begin(), answeredID.end(), wantToAnswer.getID()) != answeredID.end()) {
        return;
    }
    
    if (wantToAnswer.getAnswer() == answer){
        score+= wantToAnswer.getScore();
        this->ui->uptdateScore(score);

    }
    answeredID.push_back(wantToAnswer.getID());
    this->ui->color(wantToAnswer.getID());
}



void ParticipantWindow::populateList(std::vector<Question> myQuestions){
    this->ui->populateList(myQuestions);
    for(auto  id : answeredID){
        this->ui->color(id);
    }
}

