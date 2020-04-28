"""
@author: radu


"""
from unittest import TestCase

from store.domain.entities import Product


class TestProduct(TestCase):
    def setUp(self):
        super().setUp()
        self.__product = Product(1, "p1", 1)

    def test_entity_id(self):
        self.assertEqual(self.__product.entity_id, 1, "entity id should be 1")

    def test_name(self):
        # TODO implement test
        pass

    def test_price(self):
        # TODO implement test
        pass
