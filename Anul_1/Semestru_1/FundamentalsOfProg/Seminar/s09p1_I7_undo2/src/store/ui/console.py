"""
@author: radu


"""
import random
import traceback

from store.domain.entities import Product
from store.domain.validators import StoreException
from util.common import MyUtil


class Console(object):
    def __init__(self, product_controller, order_controller, statistics_controller,undo_controller):
        self.__product_controller = product_controller
        self.__order_controller = order_controller
        self.__statistics_controller = statistics_controller
        self.__undo_controller=undo_controller

    #
    # def run_console(self):
    #     # TODO implement an menu or cmd based console
    #
    #     self.__init_data()
    #
    #     print("all products:")
    #     self.__print_all_products()
    #
    #     print("all orders:")
    #     self.__print_all_orders()
    #
    #     print("products filtered by name (name containing the string 'p'):")
    #     MyUtil.print_list(self.__product_controller.filter_products_by_name("p"))
    #
    #     print("the cost of all orders is: ", self.__statistics_controller.compute_all_orders_cost())
    #
    #     print("the orders with the cost greater than 2 is:")
    #     MyUtil.print_list(self.__statistics_controller.filter_orders(2))
    #
    #     self.__print_sorted_orders()

    # def run_console(self):
    #     # 'testing' file operations
    #     print("all products:")
    #     self.__print_all_products()
    #
    #     # add a new product (id must be unique)
    #     r = random.randint(1, 10000000)
    #     self.__product_controller.add_product(r, "p" + str(r), r)

    def run_console(self):
        # 'test' undo

        self.__init_data()

        print("all products:")
        self.__print_all_products()

        self.__undo_controller.undo()
        print("all products:")
        self.__print_all_products()

        self.__undo_controller.undo()
        print("all products:")
        self.__print_all_products()


    def __print_all_products(self):
        MyUtil.print_list(self.__product_controller.get_all())

    def __print_all_orders(self):
        MyUtil.print_list(self.__order_controller.get_all())

    def __init_data(self):
        try:
            self.__product_controller.add_product(1, "p1", 100)
            self.__product_controller.add_product(2, "p2", 200)
            self.__product_controller.add_product(3, "bla", 300)

            self.__order_controller.add_order(1, 1, 2)
            self.__order_controller.add_order(2, 1, 3)
            self.__order_controller.add_order(3, 2, 4)

        except StoreException as se:
            print("exception when initializing data: ", se)
            traceback.print_exc()

    def __print_sorted_orders(self):
        print("the orders sorted descending by cost and ascending by name:")
        sorted_orders = self.__statistics_controller.sort_orders()
        for i in range(0, len(sorted_orders)):
            print(i + 1, sorted_orders[i])
