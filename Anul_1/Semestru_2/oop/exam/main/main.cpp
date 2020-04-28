#include "mainwindow.h"
#include <QApplication>
#include "Controller.hpp"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    
    Repository myRepository{"Participants.txt", "Questions.txt"};

    Controller myController { myRepository };
    
    MainWindow window {myController};
    
    window.show();
    window.setWindowTitle(QString::fromStdString("Presenter"));

    return a.exec();
}
