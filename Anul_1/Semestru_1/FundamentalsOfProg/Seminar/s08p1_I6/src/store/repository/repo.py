"""
@author: radu


"""
from store.domain.validators import StoreException, ValidatorException


class RepositoryException(StoreException):
    pass


class DuplicateIdException(RepositoryException):
    pass


class Repository(object):
    """Generic ``Repository`` that can be used for any entity type.
    """

    def __init__(self, validator_class):
        self.__validator_class = validator_class
        self.__entities = {}

    def find_by_id(self, entity_id):
        if entity_id in self.__entities:
            return self.__entities[entity_id]
        return None

    def save(self, entity):
        """
        Save the given entity into the repository.

        :param entity: the entity to be saved; the ``entity_id`` must not already exist.
        :return: None.
        :raises: ``RepositoryException`` - if the id already exists; ProductValidatorException - if the product
        is not valid.
        :
        """
        if not self.find_by_id(entity.entity_id) is None:
            raise DuplicateIdException("duplicate id {0}.".format(entity.entity_id))
        try:
            self.__validator_class.validate(entity)
        except ValidatorException as pve:
            raise RepositoryException(pve)
        self.__entities[entity.entity_id] = entity

    def update(self, entity):
        """
        Update the given entity.
        :param entity: the entity to be updated; the entity must already exist.
        :return: None.
        :raises: RepositoryException - if the entity does not exist.
        """
        pass

    def delete_by_id(self, entity_id):
        pass

    def get_all(self):
        return list(self.__entities.values())
