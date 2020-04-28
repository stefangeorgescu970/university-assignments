#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "GradeController.hpp"
#include "teacherwindow.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(GradeController& myController, QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_deleteButton_clicked();
    void on_addButton_clicked();

private:
    Ui::MainWindow *ui;
    GradeController myController;
    void startTeacherWindows();
    std::vector<TeacherWindow*> myTeacherWindows;
    void populateAllWindows();
};

#endif // MAINWINDOW_H
