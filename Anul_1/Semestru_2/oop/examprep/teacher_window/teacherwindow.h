#ifndef TEACHERWINDOW_H
#define TEACHERWINDOW_H

#include <QMainWindow>

namespace Ui {
class TeacherWindow;
}

class TeacherWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit TeacherWindow(QWidget *parent = 0);
    ~TeacherWindow();

private slots:
    void on_gradeButton_clicked();

private:
    Ui::TeacherWindow *ui;
};

#endif // TEACHERWINDOW_H
