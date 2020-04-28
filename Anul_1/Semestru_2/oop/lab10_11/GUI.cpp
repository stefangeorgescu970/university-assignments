#include <vector>
#include "Socks.hpp"
#include <QMessageBox>
#include "Controller.hpp"
#include "Exceptions.cpp"
#include "GUI.hpp"
#include <QGraphicsRectItem>
#include <QGraphicsScene>
#include <QGraphicsView>
#include <map>
#include <random>

SockShopQt::SockShopQt(Controller* c, QWidget* parent) :  QWidget { parent }, my_controller{}
{
	this->initGUI();
	this->my_controller = c;
	this->currentSocks = this->my_controller->get_products();
	this->populateRepoList();
}

SockShopQt::~SockShopQt()
{

}

void SockShopQt::initGUI()
{
	QHBoxLayout* layout = new QHBoxLayout{this};

	QWidget* leftWidget = new QWidget{};
	QVBoxLayout* leftSide = new QVBoxLayout{ leftWidget };


	this->repoList = new QListWidget{};
	this->repoList->setSelectionMode(QAbstractItemView::SingleSelection);


	QWidget* sockDataWidget = new QWidget{};
	QFormLayout* formLayout = new QFormLayout{sockDataWidget};


    this->shuffleRepo = new QRadioButton{"Shuffle list"};
    this->orderRepo = new QRadioButton{"Order list"};

    QGridLayout* two_buttons = new QGridLayout{};

    two_buttons->addWidget(this->shuffleRepo, 0, 0);
    two_buttons->addWidget(this->orderRepo, 0, 1);

    formLayout->addRow(two_buttons);

	this->sizeEdit = new QLineEdit{};
	this->priceEdit = new QLineEdit{};
	this->quantityEdit = new QLineEdit{};
	this->colourEdit = new QLineEdit{};
	this->photographEdit = new QLineEdit{};
	formLayout->addRow("&Size:", sizeEdit);
	formLayout->addRow("&Price:", priceEdit);
	formLayout->addRow("&Quantity:", quantityEdit);
	formLayout->addRow("&Colour:", colourEdit);
	formLayout->addRow("&Photograph:", photographEdit);


	QWidget* buttonsWidget = new QWidget{};
	QGridLayout* gridLayout = new QGridLayout{ buttonsWidget };
	this->addButton = new QPushButton("Add");
	this->deleteButton = new QPushButton("Delete");
	this->filterButton = new QPushButton("Filter");
    this->updatePriceButton = new QPushButton("Update Price");
    this->updateQuantityButton = new QPushButton("Update Quantity");
    this->priceUpdateEdit = new QLineEdit{};
    this->quantityUpdateEdit = new QLineEdit{};



	gridLayout->addWidget(addButton, 0, 0);
	gridLayout->addWidget(deleteButton, 0, 1);
	gridLayout->addWidget(filterButton, 0, 2);
    gridLayout->addWidget(updatePriceButton, 1, 0);
    gridLayout->addWidget(updateQuantityButton, 2, 0);
    gridLayout->addWidget(new QLabel{"New Price:"},1, 1);
    gridLayout->addWidget(new QLabel{"New Quantity:"}, 2, 1);
    gridLayout->addWidget(priceUpdateEdit, 1, 2);
    gridLayout->addWidget(quantityUpdateEdit, 2, 2);



	leftSide->addWidget(new QLabel{"All Socks"});
	leftSide->addWidget(repoList);
	leftSide->addWidget(sockDataWidget);
	leftSide->addWidget(buttonsWidget);


	QWidget* middleWidget = new QWidget{};
	QVBoxLayout* vLayoutMiddle = new QVBoxLayout{ middleWidget };
	this->moveOneSongButton = new QPushButton{ " Buy sock " };
    this->generateStatisticsButton = new QPushButton{ "Get Socks Statistics "};
	QWidget* upperPart = new QWidget{};
	QWidget* lowerPart = new QWidget{};
	QVBoxLayout* vLayoutUpperPart = new QVBoxLayout{ upperPart };
	vLayoutUpperPart->addWidget(this->moveOneSongButton);
	vLayoutUpperPart->addWidget(this->generateStatisticsButton);
	vLayoutMiddle->addWidget(upperPart);
	vLayoutMiddle->addWidget(lowerPart);


	QWidget* rightWidget = new QWidget{};
	QVBoxLayout* rightSide = new QVBoxLayout{ rightWidget };


	sockShop = new QListWidget{};
    this->sockShop->setSelectionMode(QAbstractItemView::SingleSelection);



	QWidget* SockShopButtonsWidget = new QWidget{};
	QGridLayout* SockShopButtonsLayout = new QGridLayout{ SockShopButtonsWidget };
    this->viewButton = new QPushButton{ "&View" };
    this->saveBasketButton = new QPushButton{ "&Save Cart to File" };
    this->viewBasketButton = new QPushButton{ "&View Cart from File" };
	SockShopButtonsLayout->addWidget(viewButton, 0, 0);
	SockShopButtonsLayout->addWidget(saveBasketButton, 1, 0);
	SockShopButtonsLayout->addWidget(viewBasketButton, 1, 1);




	rightSide->addWidget(new QLabel{ "Sock Shop" });
	rightSide->addWidget(sockShop);
	rightSide->addWidget(SockShopButtonsWidget);


	layout->addWidget(leftWidget);
	layout->addWidget(middleWidget);
	layout->addWidget(rightWidget);


	this->connectSignalsAndSlots();
}


void SockShopQt::populateRepoList()
{
	// clear the list, if there are elements in it
	if (this->repoList->count() > 0)
		this->repoList->clear();

	for (auto sock : this->currentSocks)
	{
		QString itemInList = QString::fromStdString(sock.get_colour() + " - " + to_string(sock.get_size()));
		QListWidgetItem *item3 = new QListWidgetItem(itemInList);
		//QFont font("Courier", 20, 10, true);
		//item3->setFont(font);
		this->repoList->addItem(item3);
	}

	// set the selection on the first item in the list
	if (this->currentSocks.size() > 0)
		this->repoList->setCurrentRow(0);
}

void SockShopQt::populateSockShop()
{
	// clear the list, if there are elements in it
	if (this->sockShop->count() > 0)
		this->sockShop->clear();

	for (auto sock : this->my_controller->get_cart())
	{
		QString itemInList = QString::fromStdString(sock.get_colour() + " - " + to_string(sock.get_size()) + " - " + to_string(sock.get_quantity()));
		this->sockShop->addItem(itemInList);
	}
}

int SockShopQt::getShopListSelectedIndex()
{
    if (this->sockShop->count() == 0)
        return -1;

    QModelIndexList index = this->repoList->selectionModel()->selectedIndexes();
    int idx = index.at(0).row();
    return idx;
}

int SockShopQt::getRepoListSelectedIndex()
{
	if (this->repoList->count() == 0)
		return -1;

	// get selected index
	QModelIndexList index = this->repoList->selectionModel()->selectedIndexes();
	if (index.size() == 0)
	{
		this->sizeEdit->clear();
		this->priceEdit->clear();
		this->quantityEdit->clear();
		this->colourEdit->clear();
		this->photographEdit->clear();
		return -1;
	}

	int idx = index.at(0).row();
	return idx;
}

void SockShopQt::listItemChanged()
{
	int idx = this->getRepoListSelectedIndex();
	if (idx == -1)
		return;

	std::vector<Socks> socks = this->currentSocks;


	if (idx >= socks.size())
		return;
	Socks sock = socks[idx];

	this->sizeEdit->setText(QString::fromStdString(to_string(sock.get_size())));
	this->priceEdit->setText(QString::fromStdString(to_string(sock.get_price())));
	this->quantityEdit->setText(QString::fromStdString(to_string(sock.get_quantity())));
	this->colourEdit->setText(QString::fromStdString(sock.get_colour()));
	this->photographEdit->setText(QString::fromStdString(sock.get_photograph()));
}

void SockShopQt::addNewSock()
{
	std::string colour = this->colourEdit->text().toStdString();
	std::string photograph = this->photographEdit->text().toStdString();
	int size = this->sizeEdit->text().toInt();
	int price = this->priceEdit->text().toInt();
	int quantity = this->quantityEdit->text().toInt();

	try
	{
		this->my_controller->add(size, price, quantity, colour, photograph);
		this->currentSocks = this->my_controller->get_products();
		this->populateRepoList();
	}
	catch (RepoAddException& e)
	{
		QMessageBox messageBox;
		messageBox.critical(0, "Error", QString::fromStdString(e.what()));
	}
	catch (RepoValidateException& e)
	{
		QMessageBox messageBox;
		messageBox.critical(0, "Error", e.what());
	}
}

void SockShopQt::deleteSock()
{
	std::string colour = this->colourEdit->text().toStdString();
	int size = this->sizeEdit->text().toInt();

	try
	{
		this->my_controller->remove(size, colour);
		this->currentSocks = this->my_controller->get_products();
		this->populateRepoList();
	}
	catch (RepoRemoveException& e)
	{
		QMessageBox messageBox;
		messageBox.critical(0, "Error", e.what());
	}
}

void SockShopQt::filterRepoSocks()
{
	std::string size = this->sizeEdit->text().toStdString();
	if (size == "")
	{
		this->currentSocks = this->my_controller->get_products();
		this->populateRepoList();
		return;
	}
	try {
		this->currentSocks = this->my_controller->filter_by_size(size);
	}
	catch (exception& e) {
		QMessageBox messageBox;
		messageBox.critical(0, "Error", e.what());
	}
	this->populateRepoList();
}

void SockShopQt::moveSockToSockShop()
{
	int idx = this->getRepoListSelectedIndex();
	if (idx == -1 || idx >= this->currentSocks.size())
		return;

	Socks sock = this->currentSocks[idx];
	std::vector<Socks> my_prods = this->my_controller->get_products();
	std::vector<Socks> my_cart = this->my_controller->get_cart();
	try {
		this->my_controller->add_to_cart(my_prods, my_cart, sock);
	}
	catch (AddToCartException& e) {
		QMessageBox messageBox;
		messageBox.critical(0, "Error", e.what());
	}

    this->currentSocks = this->my_controller->get_products();
	this->populateSockShop();
    this->listItemChanged();
}



void SockShopQt::updateQuantity() {
    std::string colour = this->colourEdit->text().toStdString();
    int size = this->sizeEdit->text().toInt();
    int new_quantity = this->quantityUpdateEdit->text().toInt();
    this->my_controller->update_quantity(size, colour, new_quantity);
    this->currentSocks = this->my_controller->get_products();
    this->quantityUpdateEdit->clear();
    this->listItemChanged();
}

void SockShopQt::updatePrice() {
    std::string colour = this->colourEdit->text().toStdString();
    int size = this->sizeEdit->text().toInt();
    int new_price = this->priceUpdateEdit->text().toInt();
    this->my_controller->update_price(size, colour, new_price);
    this->currentSocks = this->my_controller->get_products();
    this->priceUpdateEdit->clear();
    this->listItemChanged();
}

void SockShopQt::viewButtonPressed() {
    int index = getShopListSelectedIndex();
    Socks sock = this->my_controller->get_cart()[index];
    string command = "open -a Safari ";
    command += sock.get_photograph();
    system(command.c_str());
}



void SockShopQt::saveBasket() {
    this->my_controller->save_shopping_cart();
    QMessageBox messageBox;
    messageBox.information(0, "File save notice", "File created successfully");

}

void SockShopQt::viewBasket() {
    this->my_controller->open_shopping_cart();
}

void SockShopQt::generateStatistics() {


    QGraphicsScene* scene = new QGraphicsScene{};
    QGraphicsView* view = new QGraphicsView{};
    QLayout* layout = new QVBoxLayout{};
    QWidget* widget = new QWidget{};

    view->setScene(scene);
    layout->addWidget(view);
    widget->setLayout(layout);

    map<int, int> my_map;
    int min_size = INT8_MAX, max_size = INT8_MIN;

    for (auto sock : this->currentSocks){
        if(sock.get_size() < min_size)
            min_size = sock.get_size();
        if (sock.get_size() > max_size)
            max_size = sock.get_size();
        if(my_map.find(sock.get_size()) == my_map.end()){
            my_map.insert(pair<int, int>(sock.get_size(), 1));
        } else {
            my_map[sock.get_size()]++;
        }
    }

    int max_rep = INT8_MIN;

    for (auto pair: my_map){
        if(pair.second > max_rep)
            max_rep = pair.second;
    }

    int required_height = 65 * max_rep;

    scene->addLine( 5, 5+required_height, 5, 5);

    int current_x_pos = 55;
    int y_pos = 20 + required_height;


    for(int size = min_size; size <= max_size; size++){
        QGraphicsTextItem* size_text = new QGraphicsTextItem;
        size_text->setPos(current_x_pos, y_pos);
        size_text->setPlainText(QString::fromStdString(to_string(size)));
        scene->addItem(size_text);
        if(my_map.find(size) != my_map.end())
            scene->addRect(QRectF(current_x_pos - 15, y_pos-15 - 50*my_map[size], 50, 50*my_map[size]));
        current_x_pos += 75;
    }

    scene->addLine( 5, 5+required_height, 5+current_x_pos, 5+required_height);

    int current_y_pos =required_height - 10;
    for(int number = 0; number <= max_rep; number++){
        QGraphicsTextItem* num_text = new QGraphicsTextItem;
        num_text->setPos(-20, current_y_pos);
        num_text->setPlainText(QString::fromStdString(to_string(number)));
        scene->addItem(num_text);
        current_y_pos -= 50;
    }

    widget->show();


}

bool compare_socks(Socks& sock1, Socks& sock2){
    return sock1.get_size() < sock2.get_size();

}

void SockShopQt::shuffle_button_pressed() {

    vector<Socks> my_socks = this->my_controller->get_products();

    shuffle(my_socks.begin(), my_socks.end(), default_random_engine());

    this->currentSocks = my_socks;

    this->my_controller->set_products(my_socks);

    this->populateRepoList();

}

void SockShopQt::ordered_button_pressed() {

    vector<Socks> my_socks = this->my_controller->get_products();

    sort(my_socks.begin(), my_socks.end(), &compare_socks);

    this->currentSocks = my_socks;

    this->my_controller->set_products(my_socks);

    this->populateRepoList();

}

void SockShopQt::connectSignalsAndSlots()
{
	// add a connection: function listItemChanged() will be called when an item in the list is selected
	QObject::connect(this->repoList, SIGNAL(itemSelectionChanged()), this, SLOT(listItemChanged()));

	// add button connections
	QObject::connect(this->addButton, SIGNAL(clicked()), this, SLOT(addNewSock()));
	QObject::connect(this->deleteButton, SIGNAL(clicked()), this, SLOT(deleteSock()));
	QObject::connect(this->filterButton, SIGNAL(clicked()), this, SLOT(filterRepoSocks()));

	QObject::connect(this->moveOneSongButton, SIGNAL(clicked()), this, SLOT(moveSockToSockShop()));

    QObject::connect(this->updateQuantityButton, SIGNAL(clicked()), this, SLOT(updateQuantity()));
    QObject::connect(this->updatePriceButton, SIGNAL(clicked()), this, SLOT(updatePrice()));


    QObject::connect(this->viewButton, SIGNAL(clicked()), this, SLOT(viewButtonPressed()));
    QObject::connect(this->saveBasketButton, SIGNAL(clicked()), this, SLOT(saveBasket()));
    QObject::connect(this->viewBasketButton, SIGNAL(clicked()), this, SLOT(viewBasket()));


    QObject::connect(this->generateStatisticsButton, SIGNAL(clicked()), this, SLOT(generateStatistics()));

    QObject::connect(this->shuffleRepo, SIGNAL(clicked()), this, SLOT(shuffle_button_pressed()));
    QObject::connect(this->orderRepo, SIGNAL(clicked()), this, SLOT(ordered_button_pressed()));
}