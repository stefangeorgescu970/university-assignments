#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "Question.hpp"
#include "Controller.hpp"
#include "participantwindow.h"
namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(Controller myController, QWidget *parent = 0);
    ~MainWindow();

    void populateList(std::vector<Question> myQuestions);
    
    void runParticipantWindows();
    
    void updateWindows(Question& question);
    
    void populateParticipant(std::vector<Question> myQuestions);
    
private slots:
    void on_addButton_clicked();
    

private:
    Ui::MainWindow *ui;
    std::vector<ParticipantWindow* >participantWindows;
    Controller myController;
};

#endif // MAINWINDOW_H
