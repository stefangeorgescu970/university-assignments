#ifndef DIALOG_H
#define DIALOG_H

#include <QDialog>

namespace Ui {
class Dialog;
}

class Dialog : public QDialog
{
    Q_OBJECT

public:
    explicit Dialog(QWidget *parent = 0);
    ~Dialog();
    
    bool getDecision();

private:
    Ui::Dialog *ui;
    bool decision;
    
private slots:
    void on_yesButton_clicked();
    
    void on_noButton_clicked();
};

#endif // DIALOG_H
