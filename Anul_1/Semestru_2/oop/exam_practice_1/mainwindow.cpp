#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QLabel>
#include <iostream>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_eudaugraf_clicked()
{
    int decision;
    
    QWidget* widget = new QWidget{};
    QLayout* button_layout = new QHBoxLayout{};
    QWidget* button_widget = new QWidget{};
    QLayout* layout = new QVBoxLayout{};
    
    
    button_widget->setLayout(button_layout);
    widget->setLayout(layout);
    
    widget->setWindowTitle("Enquiry");
    
    QPushButton* yes_b = new QPushButton{"Yes"};
    QPushButton* no_b = new QPushButton{"No"};
    
    button_layout->addWidget(yes_b);
    button_layout->addWidget(no_b);
    
    layout->addWidget(new QLabel{"Esti pe zona?"});
    layout->addWidget(button_widget);
    
    widget->show();
    
    
    connect(yes_b, &QPushButton::clicked, [this, &decision, widget]{
        std::cout<<"yes\n"; widget->close();
    });
    
    connect(no_b, &QPushButton::clicked, [this, &decision, widget]{
        std::cout<<"no\n"; widget->close();
    });
    
}
