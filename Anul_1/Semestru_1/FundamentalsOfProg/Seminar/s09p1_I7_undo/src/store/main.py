"""
@author: radu

ProductStore

Write an application that manages the products and orders from a product store.
Product (product_id, name, price)
Order (order_id, product_id, quantity)

The application should allow to:

F1: add new products
F2: delete products
F3: update products
F4: print all products

F5: make an order
F6: delete an order
F7: update an order
F8: print all orders

F9: filter products (e.g: print all products whose name contain a given string)

F10: compute the cost of all orders
F11: filter orders (e.g:return all orders (crt., product name, quantity, cost) with the cost greater than 2)

F12_: validators and exceptions (ProductValidator)

F13_: class Order with properties

F14_: file repository

F15: find the product that was ordered most times.

F16: sort orders (product name, quantity, cost) descending after the cost (i.e., order cost) and alphabetically
after product name.

F17_: add __eq__ and __ne__
F18_: use validators (ProductValidator)

F19_: unittest

F20_: base entity

----------------------------------------------------------------------------------------------
I1: F1, F4
I2: F12_, F17_, F18_, F9
I3: F13_, F5, F8

I4: F10

I5: F19_
I6: F11, F16
I7: F20_, F14_
I8: F2, F3, F6, F7, F15
"""
import traceback

from store.controller.order_controller import OrderController
from store.controller.product_controller import ProductController
from store.controller.statistics_controller import StatisticsController
from store.controller.undo import UndoController
from store.domain.validators import ProductValidator, OrderValidator
from store.repository.file_repository import ProductFileRepository
from store.repository.repo import Repository
from store.ui.console import Console

if __name__ == "__main__":
    try:
        # print(os.getcwd())

        undo_controller = UndoController()

        product_repository = Repository(ProductValidator)
        # product_repository = ProductFileRepository(ProductValidator, "../../data/products")

        product_controller = ProductController(product_repository, undo_controller)

        order_repository = Repository(OrderValidator)
        order_controller = OrderController(order_repository, product_repository)

        statistics_controller = StatisticsController(product_repository, order_repository)

        console = Console(product_controller, order_controller, statistics_controller,undo_controller)

        console.run_console()


    except Exception as ex:
        print("exception: ", ex)
        traceback.print_exc()

    print("bye")
