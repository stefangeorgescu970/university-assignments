"""
@author: radu


"""
from store.domain.entities import Product


class ProductController(object):
    def __init__(self, product_repository, undo_controller):
        self.__product_repository = product_repository
        self.__undo_controller = undo_controller

    def add_product(self, product_id, name, price):
        product = Product(product_id, name, price)
        self.__product_repository.save(product)

        self.__undo_controller.register_operation(self.add_product, self.delete_product, product_id)

    def delete_product(self, product_id):
        self.__product_repository.delete_by_id(product_id)

    def get_all(self):
        return self.__product_repository.get_all()

    def filter_products_by_name(self, name):
        """Return all products whose name contain the string ``name``
        """
        return list(filter(lambda p: name in p.name, self.__product_repository.get_all()))
