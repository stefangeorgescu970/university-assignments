"""
Created on 19/12/2016
@author Stefan
"""
class Person(object):
    def __init__(self, person_id, immunization_status, health_status):
        self.__person_id = person_id
        self.__immunization_status = immunization_status
        self.__health_status = health_status
        self.__days_ill = 0

    @property
    def id(self):
        return self.__person_id

    @property
    def is_immune(self):
        if self.__immunization_status == "vaccinated":
            return True
        return False

    @property
    def is_healthy(self):
        if self.__health_status == 'ill':
            return False
        return True

    @property
    def days_ill(self):
        return self.__days_ill

    @days_ill.setter
    def days_ill(self, value):
        self.__days_ill = value

    def get_ill(self):
        self.__health_status = 'ill'

    def get_well(self):
        self.__health_status = 'healthy'

    def vaccinate(self):
        self.__immunization_status = 'vaccinated'

    def __str__(self):
        return str(self.id) + ',' + self.__immunization_status + ',' + self.__health_status
