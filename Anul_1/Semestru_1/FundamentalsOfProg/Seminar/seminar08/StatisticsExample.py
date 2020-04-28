from seminar08.repository.Repository import Repository
from seminar08.domain.Client import ClientValidator
from seminar08.domain.Car import CarValidator
from seminar08.domain.Rental import RentalValidator
from seminar08.controller.ClientController import ClientController
from seminar08.controller.CarController import CarController
from seminar08.controller.RentalController import RentalController
from datetime import datetime

def statisticsExample():
    """
    An example for the creation of statistics.
    Several cars, clients and rentals are created and then statistics are calculated over them.
    
    Implement the following statistics:
        - "Most rented cars". The list of cars, sorted by the number of times they were rented
        - "Most rented cars". The list of cars, sorted by the number of days they were rented
        - "Most rented car make". The list of car makes, sorted by the number of rentals
    
    Follow the code below and figure out how it works!
    """

    """
        1. We initialize the required layers of the application
    """

    '''
    Start client Controller
    '''
    clientRepo = Repository()
    clientValidator = ClientValidator()
    clientController = ClientController(clientValidator, clientRepo)
    
    clientController.create(100, "1820203556699", "Aaron")
    clientController.create(101, "2750102885566", "Bob")
    clientController.create(102, "1820604536579", "Carol")

    aaron = clientRepo.find(100)
    bob = clientRepo.find(101)
    carol = clientRepo.find(102)

    '''
    Start car Controller
    '''
    carRepo = Repository()
    carValidator = CarValidator()
    carController = CarController(carValidator, carRepo)

    carController.create(200, "CJ 01 AAA", "Audi", "A3")
    carController.create(201, "CJ 01 BBB", "Audi", "A4")
    carController.create(202, "CJ 01 CCC", "Audi", "A5")
    carController.create(203, "CJ 01 DDD", "Audi", "A6")
    carController.create(204, "CJ 01 EEE", "Audi", "A7")
    carController.create(205, "CJ 01 FFF", "VW", "Polo")
    carController.create(206, "CJ 01 GGG", "VW", "Passat")
    carController.create(207, "CJ 01 HHH", "VW", "Golf")
    carController.create(208, "CJ 01 ERT", "Dacia", "Lodgy")
    carController.create(209, "CJ 01 YTH", "Dacia", "Duster")

    audiA3 = carRepo.find(200)
    audiA4 = carRepo.find(201)
    audiA5 = carRepo.find(202)
    audiA6 = carRepo.find(203)
    vwpolo = carRepo.find(205)
    vwpassat = carRepo.find(206)
    vwgolf = carRepo.find(207)
    dacialodgy = carRepo.find(208)
    daciaduster = carRepo.find(209)

    '''
    Start rental Controller
    '''
    rentRepo = Repository()
    rentValidator = RentalValidator()
    rentController = RentalController(rentValidator, rentRepo, carRepo, clientRepo)

    rentController.createRental(300, aaron, audiA3, datetime.strptime("2015-11-20", "%Y-%m-%d"), datetime.strptime("2015-11-22", "%Y-%m-%d"))
    rentController.createRental(301, carol, audiA5, datetime.strptime("2015-11-24", "%Y-%m-%d"), datetime.strptime("2015-11-25", "%Y-%m-%d"))
    rentController.createRental(302, carol, audiA6, datetime.strptime("2015-12-10", "%Y-%m-%d"), datetime.strptime("2015-12-12", "%Y-%m-%d"))
    rentController.createRental(303, aaron, audiA4, datetime.strptime("2015-11-21", "%Y-%m-%d"), datetime.strptime("2015-11-25", "%Y-%m-%d"))
    rentController.createRental(304, aaron, audiA3, datetime.strptime("2015-11-24", "%Y-%m-%d"), datetime.strptime("2015-11-27", "%Y-%m-%d"))
    rentController.createRental(305, bob, audiA5, datetime.strptime("2015-11-26", "%Y-%m-%d"), datetime.strptime("2015-11-27", "%Y-%m-%d"))
    rentController.createRental(306, carol, audiA6, datetime.strptime("2015-12-15", "%Y-%m-%d"), datetime.strptime("2015-12-20", "%Y-%m-%d"))
    rentController.createRental(307, bob, audiA4, datetime.strptime("2015-12-01", "%Y-%m-%d"), datetime.strptime("2015-12-10", "%Y-%m-%d"))
    rentController.createRental(308, carol, audiA4, datetime.strptime("2015-12-11", "%Y-%m-%d"), datetime.strptime("2015-12-15", "%Y-%m-%d"))
    rentController.createRental(309, aaron, audiA5, datetime.strptime("2015-11-28", "%Y-%m-%d"), datetime.strptime("2015-12-02", "%Y-%m-%d"))

    rentController.createRental(310, aaron, vwpolo, datetime.strptime("2015-11-20", "%Y-%m-%d"), datetime.strptime("2015-11-22", "%Y-%m-%d"))
    rentController.createRental(311, carol, vwgolf, datetime.strptime("2015-11-24", "%Y-%m-%d"), datetime.strptime("2015-11-25", "%Y-%m-%d"))
    rentController.createRental(312, carol, vwpassat, datetime.strptime("2015-12-10", "%Y-%m-%d"), datetime.strptime("2015-12-12", "%Y-%m-%d"))
    rentController.createRental(313, aaron, dacialodgy, datetime.strptime("2015-11-21", "%Y-%m-%d"), datetime.strptime("2015-11-25", "%Y-%m-%d"))
    rentController.createRental(314, aaron, vwpolo, datetime.strptime("2015-11-24", "%Y-%m-%d"), datetime.strptime("2015-11-27", "%Y-%m-%d"))
    rentController.createRental(315, bob, vwgolf, datetime.strptime("2015-11-26", "%Y-%m-%d"), datetime.strptime("2015-11-27", "%Y-%m-%d"))
    rentController.createRental(316, carol, vwgolf, datetime.strptime("2015-12-15", "%Y-%m-%d"), datetime.strptime("2015-12-20", "%Y-%m-%d"))
    rentController.createRental(317, bob, daciaduster, datetime.strptime("2015-12-01", "%Y-%m-%d"), datetime.strptime("2015-12-10", "%Y-%m-%d"))
    rentController.createRental(318, carol, daciaduster, datetime.strptime("2015-12-11", "%Y-%m-%d"), datetime.strptime("2015-12-15", "%Y-%m-%d"))
    rentController.createRental(319, aaron, vwpassat, datetime.strptime("2015-11-28", "%Y-%m-%d"), datetime.strptime("2015-12-02", "%Y-%m-%d"))

    """
    Statistic 1:
        - "Most rented cars". The list of cars, sorted by the number of times they were rented
    """
    print("Most rented cars. The list of cars, sorted by the number of times they were rented")
    print("Times".ljust(10) + " Car".ljust(40))
    for cr in rentController.mostOftenRentedCars(): 
        print (cr)

    print("-"*70)

    """
    Statistic 2:
        - "Most rented cars". The list of cars, sorted by the number of days they were rented
    """
    print("Most rented cars. The list of cars, sorted by the number of days they were rented")
    print("Days".ljust(10) + " Car".ljust(40))
    for cr in rentController.mostRentedCars():
        print (cr)

    print("-"*70)
    
    """
    Statistic 3:
        - "Most rented car make". The list of car makes, sorted by the number of rentals
    """
    print("Most rented car make. The list of car makes, sorted by the number of rentals")
    print("Times".ljust(10) + " Car make".ljust(40))
    for cr in rentController.mostOftenRentedCarMake():
        print (cr)

statisticsExample()
















