"""
@author: radu


"""
from store.domain.validators import StoreException


class RepositoryException(StoreException):
    pass


class Repository(object):
    def __init__(self, validator_class):
        self.__validator_class = validator_class
        self.__entities = {}

    def find_by_id(self, entity_id):
        if entity_id in self.__entities:
            return self.__entities[entity_id]
        return None

    def save(self, entity):
        if not self.find_by_id(entity.entity_id) is None:
            raise RepositoryException("duplicate id {0}.".format(entity.entity_id))
        self.__validator_class.validate(entity)
        self.__entities[entity.entity_id] = entity

    def update(self, entity_id, entity):
        pass

    def delete_by_id(self, entity_id):
        pass

    def get_all(self):
        return self.__entities.values()
