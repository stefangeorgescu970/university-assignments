import copy

from studentRegister.domain.validators import RegisterException


class RepositoryException(RegisterException):
    pass


class Repository(object):
    """
    Keeps program data and modifies t
    """
    def __init__(self, validator_class):
        """
        Initialises the data structure for students and disciplines
        :param validator_class: Link towards validators.
        """
        self.__validator_class = validator_class
        self.__entities = {}

    def find_by_id(self, entity_id):
        """
        Searches for an entry in the record by its id.
        :param entity_id: an integer
        :return: the entity if it exists, or None if it doesn't
        """
        if entity_id in self.__entities:
            return self.__entities[entity_id]
        return None

    def save(self, entity):
        """
        Saves a new entity to the list.
        :param entity: a valid entity. If not, an exception will be raised.
        """
        if not self.find_by_id(entity.entity_id) is None:
            raise RepositoryException("Duplicate ID {0}.". format(entity.entity_id))
        self.__validator_class.validate(entity)
        self.__entities[entity.entity_id] = entity

    # Update func will only be used for students, disciplines and grades.
    def update(self, entity_id, entity):
        """
        Updates an existing entity.
        :param entity_id: The id of the entity that needs to be updated.
        :param entity: The new entity
        """
        if not self.find_by_id(entity_id) is None:
            old_entity = copy.deepcopy(self.__entities[entity_id])
            self.__entities[entity_id] = entity
            return old_entity
        else:
            raise RepositoryException("There is no entity with the mentioned ID.")

    def delete_by_id(self, entity_id):
        """
        Deletes an entity with a given id.
        :param entity_id: an int
        """
        if len(self.__entities) == 0:
            raise RepositoryException("There are no entities left in the registry.")
        if entity_id in self.__entities:
            entity = self.__entities[entity_id]
            del self.__entities[entity_id]
            return entity
        else:
            raise RepositoryException("There is no entity with the mentioned ID.")

    def get_all(self):
        """
        Returns all the entities as a list as a dict_values object.
        """
        return list(self.__entities.values())

    # this func will only be used for students and disciplines
    def find_by_name(self, entity_name):
        """
        Returns a list of entities that partially match the given string
        :param entity_name: a string
        :return: a list of entities
        """
        entityList = []
        for item in self.__entities.values():
            if entity_name in item.name:
                entityList.append(item)
        return entityList

    # will only be used by grades repository
    def get_all_grades_by_discipline(self, discipline_id):
        """
        Will return a list with all the grades registered for a given discipline id
        :param discipline_id: an int
        :return: the up mentioned list
        """
        grades = []
        for grade in self.__entities.values():
            index = grade.entity_id.find('.')
            idToCheck = int(grade.entity_id[:index])
            if discipline_id == idToCheck:
                grades.append(grade.grade_value)
        return grades

    # will only be used by grades repository
    def get_all_grades_by_student(self, student_id):
        """
        Will return a list with all the grades received by a given student
        :param student_id: the student
        :return: his grades. Gosh, horror.
        """
        grades = []
        for grade in self.__entities.values():
            index = grade.entity_id.find('.')
            idToCheck = int(grade.entity_id[index+1:])
            if student_id == idToCheck:
                grades.append(grade.grade_value)
        return grades
