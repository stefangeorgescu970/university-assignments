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

    # @entity_id.setter
    # def entity_id(self, value):
    #     self.__entity_id = value

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
        self.__price = value

    def __str__(self, *args, **kwargs):
        return "({0},{1},{2})".format(self.entity_id, self.name, self.price)

    def __eq__(self, other):
        return self.entity_id == other.entity_id

    def __ne__(self, other):
        return not self.__eq__(other)


class Order(object):
    def __init__(self, order_id, product_id, quantity):
        self.__order_id = order_id
        self.__product_id = product_id
        self.__quantity = quantity

    @property
    def entity_id(self):
        return self.__order_id

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    def __str__(self):
        return "({0}, {1}, {2})".format(self.entity_id, self.product_id, self.quantity)

    def __eq__(self, other):
        return self.entity_id == other.entity_id

    def __ne__(self, other):
        return not self.__eq__(other)
