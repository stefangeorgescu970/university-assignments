#include "participantwindow.h"
#include "ui_participantwindow.h"

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

void ParticipantWindow::on_pushButton_clicked()
{

}

void ParticipantWindow::on_questionList_itemSelectionChanged()
{

}
