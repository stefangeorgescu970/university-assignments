from seminar08.domain.Car import Car

class CarController:
    def __init__(self, validator, repository):
        self.__validator = validator
        self.__repository = repository
        
    def create(self, clientId, licenseNumber, make, model):
        car = Car(clientId, licenseNumber, make, model)
        self.__validator.validate(car)
        self.__repository.store(car)

    def delete(self, clientId):
        self.__repository.delete(clientId)
        
    def findByID(self, clientId):
        return self.__repository.find(clientId)
        
    def filter(self, make, model):
        return self.__repository.filter(make, model)
        
    def update(self, client):
        self.__repository.update(client)
        
    def getCarCount(self):
        return len(self.__repository)
