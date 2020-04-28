"""
@author: radu


"""


class Product(object):
    def __init__(self, entity_id, name, price):
        self.__entity_id = entity_id
        self.__name = name
        self.__price = price

    @property
    def entity_id(self):
        return self.__entity_id

    @entity_id.setter
    def entity_id(self, value):
        self.__entity_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        pass

    def __str__(self, *args, **kwargs):
        return "({0},{1},{2})".format(self.entity_id, self.name, self.price)
