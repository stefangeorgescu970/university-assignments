#include "mainwindow.h"
#include "teacherwindow.h"
#include <QApplication>
#include "GradeRepository.hpp"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    GradeRepository myRepo{"Students.txt","Teachers.txt"};
    GradeController myController{myRepo};
    MainWindow window{myController};
    window.show();
    return a.exec();
}
