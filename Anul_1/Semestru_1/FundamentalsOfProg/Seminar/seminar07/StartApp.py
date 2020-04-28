'''
Created on Nov 12, 2016

@author: Arthur
'''
from datetime import date

from controller.RentalController import RentalController
from domain.Rental import Rental
from repository.Repository import Repository
from domain.Car import Car
from domain.Client import Client

carRepo = Repository()
clientRepo = Repository()
rentalRepo = Repository()
rentalCont = RentalController(rentalRepo)

# carRepo.store(Car(1, "AB 01 RTY", "Mazda", "CX-3"))
# carRepo.store(Car(2, "NT 99 PUX", "Dacia", "Dokker"))

# clientRepo.store(Client(1001, "2850369887452", "Maria Popescu"))
# clientRepo.store(Client(1002, "2880365882446", "Ion Andone"))

def clientListGenerator():
    clientList = ["Stefan Georgescu", "Maria Mautino", "David Harambe", "Adrian Moldovan", "Ion Andone",
                "Cristian Nacu", "Monica Grigorovici", "Diana Dragos", "Calin Badea"]

    cnpList = ["1970704035266", "1970704035266", "1970704035266", "1970704035266", "1970704035266", "1970704035266",
               "1970704035266", "1970704035266", "1970704035266"]
    return (clientList, cnpList)


def carListGenerator():
    makeList = ["Mazda", "Mazda", "Ford", "Ford", "Ford", "Ford", "Honda", "Honda", "Honda"]
    modelList = ["CX-3", "6", "Mondeo", "Fiesta", "Transit", "Focus", "Civic", "Accord", "NewOne"]
    licensePlate = ["AG 04 SPG", "BC 29 ARI", "AG 07 ASJ", "VL 05 WMV", "AG 03 KIK", "BV 29 MAS", "AG 07 CDS",
                    "SM 98 ADI", "AG 04 EDY"]
    return licensePlate, makeList, modelList


def init_clients():
    (clientList, cnpList) = clientListGenerator()
    for index in range(0, len(clientList)):
        clientRepo.store(Client(index+1, cnpList[index], clientList[index]))

def init_cars():
    (licensePlate, makeList, modelList) = carListGenerator()
    for index in range(0, len(licensePlate)):
        carRepo.store(Car(index+1, licensePlate[index], makeList[index], modelList[index]))

def init_rental():
    startDay = 1
    returnDay = 2
    indexRent = 1
    for index, car in enumerate(carRepo.getAll()):
        rentalRepo.store(Rental(indexRent, date(2016,11, startDay), date(2016,11, returnDay), clientRepo.getAll()[index], car))
        indexRent += 1
        startDay += 1
        returnDay += 2


init_cars()
init_clients()
init_rental()

print("Init done")

print("This is our car repo:")
print(carRepo)


print("This is our client repo:")
print(clientRepo)

print("This is the rental repo:")
print(rentalRepo)

for item in rentalCont.ordered_list():
    print("\n"
          "RENTAL:")
    print(item[0], " for a number of ", item[1])
