from seminar08.domain.Client import Client

class ClientController:
    def __init__(self, validator, repository):
        self.__validator = validator
        self.__repository = repository

    def create(self, clientId, cnp, name):
        client = Client(clientId, cnp, name)
        self.__validator.validate(client)
        self.__repository.store(client)

    def delete(self, clientId):
        self.__repository.delete(clientId)
        
    def update(self, client):
        self.__repository.update(client)
       
    def getClientCount(self):
        return len(self.__repository)
        
    
        
            
        
