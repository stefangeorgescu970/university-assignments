#ifndef PARTICIPANTWINDOW_H
#define PARTICIPANTWINDOW_H

#include <QMainWindow>
#include "Question.hpp"

namespace Ui {
class ParticipantWindow;
}

class ParticipantWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit ParticipantWindow(QWidget *parent = 0);
    ~ParticipantWindow();
    void populateList(std::vector<Question> myQuestions);
    void updateWindow(Question& question);

private slots:
    void on_pushButton_clicked();
    void on_questionList_itemSelectionChanged();

private:
    Ui::ParticipantWindow *ui;
    std::vector<int> answeredID;
    int score = 0;
};

#endif // PARTICIPANTWINDOW_H
