#ifndef PARTICIPANTWINDOW_H
#define PARTICIPANTWINDOW_H

#include <QMainWindow>

namespace Ui {
class ParticipantWindow;
}

class ParticipantWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit ParticipantWindow(QWidget *parent = 0);
    ~ParticipantWindow();

private slots:
    void on_pushButton_clicked();

    void on_questionList_itemSelectionChanged();

private:
    Ui::ParticipantWindow *ui;
};

#endif // PARTICIPANTWINDOW_H
