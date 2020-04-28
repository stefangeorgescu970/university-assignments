"""
@author: radu


"""
from itertools import count

from store.domain.dto import OrderDTO, OrderAssembler


class StatisticsController(object):
    def __init__(self, product_repository, order_repository):
        self.__product_repository = product_repository
        self.__order_repository = order_repository

    def compute_all_orders_cost(self):
        cost, all_orders = 0, self.__order_repository.get_all()
        for o in all_orders:
            product = self.__product_repository.find_by_id(o.product_id)
            cost = cost + product.price * o.quantity
        return cost

    def filter_orders(self, cost):
        """
        :param cost:integer
        :return: all OrderDTOs with the cost greater than the given cost.
        """
        dtos = self.__create_order_dtos()
        return list(filter(lambda dto: dto.cost > cost, dtos))

    def __create_order_dtos(self):
        orders = self.__order_repository.get_all()
        dtos = []
        for o in orders:
            product = self.__product_repository.find_by_id(o.product_id)
            order_dto = OrderAssembler.create_order_dto(product, o)
            dtos.append(order_dto)
        return dtos

    def sort_orders(self):
        """
        :return: a list of OrderDTOs (product_name, quantity, cost) sorted descending after the cost (i.e., order cost)
        and alphabetically after product name
        """
        dtos = self.__create_order_dtos()

        # dtos sorted by cost - ascending
        # return sorted(dtos, key=lambda dto: dto.cost)

        # dtos sorted by cost descending
        # return sorted(dtos, key=lambda dto: dto.cost, reverse=True)

        # dtos sorted by cost and name both ascending
        # return sorted(dtos, key=lambda dto: (dto.cost, dto.product_name))

        # dtos sorted by cost and name both descending
        # return sorted(dtos, key=lambda dto: (dto.cost, dto.product_name), reverse=True)

        # dtos sorted by cost descending and name ascending
        def less_than(dto1, dto2):
            if dto1.cost == dto2.cost:
                return dto1.product_name < dto2.product_name
            return dto1.cost > dto2.cost

        OrderDTO.__lt__ = less_than
        OrderDTO.__gt__ = lambda dto1, dto2: not less_than(dto1, dto2)

        l = sorted(dtos)

        OrderDTO.__lt__ = object.__lt__
        OrderDTO.__gt__ = object.__gt__

        return l

