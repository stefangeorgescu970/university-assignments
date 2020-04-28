#include "participantwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    ParticipantWindow w;
    w.show();

    return a.exec();
}
