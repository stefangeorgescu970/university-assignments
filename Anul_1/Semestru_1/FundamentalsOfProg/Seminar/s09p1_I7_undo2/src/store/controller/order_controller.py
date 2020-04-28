"""
@author: radu


"""
from store.domain.entities import Order
from store.domain.validators import StoreException


class OrderControllerException(StoreException):
    pass


class OrderController(object):
    def __init__(self, order_repository, product_repository):
        self.__order_repository = order_repository
        self.__product_repository = product_repository

    def add_order(self, order_id, product_id, quantity):
        if self.__product_repository.find_by_id(product_id) is None:
            raise OrderControllerException("product id {0} does not exist".format(product_id))
        o = Order(order_id, product_id, quantity)
        self.__order_repository.save(o)

    def get_all(self):
        return self.__order_repository.get_all()
