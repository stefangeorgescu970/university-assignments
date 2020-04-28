#include "dialog.h"
#include "ui_dialog.h"
#include <iostream>

Dialog::Dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Dialog)
{
    ui->setupUi(this);
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_yesButton_clicked()
{
    decision = true;
    std::cout<<"YES";
    this->close();
    
}

void Dialog::on_noButton_clicked()
{
    decision = false;
    std::cout<<"FALSE";
    this->close();
    
}

bool Dialog::getDecision(){
    return decision;
}
