"""
@author: radu


"""
import traceback

from store.domain.validators import StoreException


class Console(object):
    def __init__(self, product_controller):
        self.__product_controller = product_controller

    def run_console(self):
        # TODO implement an menu or cmd based console

        # add some products
        try:
            self.__product_controller.add_product(1, "p1", 100)
            self.__product_controller.add_product(2, "p2", 200)
            self.__product_controller.add_product(1, "p3", 300)
        except StoreException as se:
            print("exception when adding products: ", se)
            traceback.print_exc()

        # print all products
        for p in self.__product_controller.get_all():
            print(p)
