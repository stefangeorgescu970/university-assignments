"""
@author: radu


"""
from unittest import TestCase

from store.domain.entities import Product
from store.domain.validators import ProductValidator
from store.repository.repo import Repository, DuplicateIdException, RepositoryException


class TestRepository(TestCase):
    def setUp(self):
        super().setUp()
        self.__repository = Repository(ProductValidator)

    def test_find_by_id(self):
        # TODO implement test
        pass

    def test_save(self):
        p = Product(1, "p1", 100)
        self.__repository.save(p)
        self.assertEqual(len(self.__repository.get_all()), 1, "there should be 1 product in the repository")

        # check if DuplicateIdException is raised
        p2 = Product(1, "p1", 100)
        self.assertRaises(DuplicateIdException, self.__repository.save, p2)

        # check if ValidatorException is caught i.e., if RepositoryException is raised (version 1)
        p3 = Product("3", "p1", 100)
        try:
            self.__repository.save(p3)
            self.fail("execution should not arrive here")
        except RepositoryException:
            self.assertTrue(True, "RepositoryException should have been raised")

        # check if RepositoryException is raised (version 2)
        self.assertRaises(RepositoryException, self.__repository.save, p3)

    def test_update(self):
        # TODO implement test
        pass

    def test_delete_by_id(self):
        # TODO implement test
        pass

    def test_get_all(self):
        # TODO implement test
        pass
