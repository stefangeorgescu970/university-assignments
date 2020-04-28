"""
@author: radu


"""
from store.domain.entities import Product
from store.repository.repo import Repository


class ProductFileRepository(Repository):
    def __init__(self, validator_class, file_name):
        super().__init__(validator_class)
        self.__file_name = file_name

        self.__load_from_file()

    def __load_from_file(self):
        # TODO handle exceptions - file not found, corrupted file etc.
        with open(self.__file_name) as f:
            for line in f:
                # there is one product/line, the attributes are separated by comas.
                attributes = line.split(",")
                product = Product(int(attributes[0]), attributes[1], int(attributes[2]))
                super().save(product)

    def save(self, product):
        super().save(product)

        self.__save_to_file(product)

    def __save_to_file(self, product):
        with open(self.__file_name, "a") as f:
            f.write("\n" + str(product.entity_id) + "," + product.name + "," + str(product.price))


class OrderFileRepository(Repository):
    pass
