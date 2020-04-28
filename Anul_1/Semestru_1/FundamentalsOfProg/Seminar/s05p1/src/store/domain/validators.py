"""
@author: radu


"""


class StoreException(Exception):
    pass


class ProductValidatorException(StoreException):
    pass


class ProductValidator(object):
    @staticmethod
    def validate(product):
        if not type(product.entity_id) is int:
            raise ProductValidatorException("id must be an int")

            # TODO other validations
