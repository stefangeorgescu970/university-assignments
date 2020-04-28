#ifndef PLAYLISTQT_H
#define PLAYLISTQT_H

#include <QtWidgets/QMainWindow>
#include "Controller.hpp"
#include <QListWidget>
#include <QFormLayout>
#include <QLineEdit>
#include <QPushButton>
#include <QLabel>
#include <QRadioButton>



class SockShopQt : public QWidget {

    Q_OBJECT

public:
    SockShopQt(Controller* c, QWidget *parent = 0);
	~SockShopQt();

private:
	Controller* my_controller;
	std::vector<Socks> currentSocks;

	QListWidget* repoList;
	QLineEdit* sizeEdit;
	QLineEdit* priceEdit;
	QLineEdit* quantityEdit;
	QLineEdit* colourEdit;
	QLineEdit* photographEdit;
	QLineEdit* priceUpdateEdit;
	QLineEdit* quantityUpdateEdit;
	QPushButton* addButton;
	QPushButton* deleteButton;
	QPushButton* filterButton;
	QPushButton* moveOneSongButton;
    QPushButton* updateQuantityButton;
    QPushButton* updatePriceButton;
    QPushButton* viewButton;
    QPushButton* saveBasketButton;
    QPushButton* viewBasketButton;
    QPushButton* generateStatisticsButton;
    QRadioButton* shuffleRepo;
    QRadioButton* orderRepo;
	QListWidget* sockShop;


	void initGUI();
	void populateRepoList();
	void populateSockShop();
	int getRepoListSelectedIndex();
    int getShopListSelectedIndex();

	void connectSignalsAndSlots();

private slots:
    void shuffle_button_pressed();

    void ordered_button_pressed();

	void listItemChanged();

	void addNewSock();
	void deleteSock();

	void filterRepoSocks();

	void moveSockToSockShop();

    void updateQuantity();

    void updatePrice();

    void viewButtonPressed();


    void saveBasket();

    void viewBasket();

    void generateStatistics();
};

#endif // PLAYLISTQT_H
