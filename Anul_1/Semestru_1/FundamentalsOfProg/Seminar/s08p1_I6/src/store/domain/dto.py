"""
@author: radu


"""


class OrderAssembler(object):
    @staticmethod
    def create_order_dto(product, order):
        """
        :param product: Product
        :param order: Order
        :return: OrderDTO
        """
        return OrderDTO(product.name, order.quantity, product.price * order.quantity)

    @staticmethod
    def update_product(product, order_dto):
        """
        :param product:
        :param order_dto:
        :return: None
        """
        # TODO implement method
        pass

    @staticmethod
    def update_order(order, order_dto):
        """
        :param order:
        :param order_dto:
        :return: None
        """
        # TODO implement method
        pass


class OrderDTO(object):
    def __init__(self, product_name, quantity, cost):
        self.__product_name = product_name
        self.__quantity = quantity
        self.__cost = cost

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, value):
        self.__product_name = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        self.__cost = value

    def __str__(self):
        return "({0},{1},{2})".format(self.product_name, self.quantity, self.cost)

    # def __lt__(self, other):
    #     if self.cost == other.cost:
    #         return self.product_name < other.product_name
    #     return self.cost > other.cost
