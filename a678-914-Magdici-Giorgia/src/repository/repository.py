
from src.domain.validators import LibraryValidatorException


class RepositoryException(Exception):
    pass


class Repository(object):
    """
    This class heps us manage all the data about the books, the clients or the rentals we have.
    """

    def __init__(self, validator_class):
        self.__validator_class = validator_class
        self._entities = {}

    def find_by_id(self, entity_id):
        """
        This function tries to find an entity, knowing its id.
        :param entity_id: the id
        :return: the entity if it exists, None otherwise
        """
        if entity_id in self._entities:
            return self._entities[entity_id]
        return None

    def add(self, entity):
        """
        Adds an entity (book/client/rental) to the repository.
        """
        if self.find_by_id(entity.id) is not None:
            raise RepositoryException("duplicated id {0}.".format(entity.id))
        try:
            self.__validator_class.validate(entity)
            self._entities[entity.id] = entity
        except LibraryValidatorException as lve:
            print(lve)


    def update(self, entity_id, entity):
        """
        Updates an element from the repository, knowing the element's id, and replaces it with the new item.
        """
        if self.find_by_id(entity_id) is None:
            raise RepositoryException("Nonexistent id {0}".format(entity_id))
        try:
            self.__validator_class.validate(entity)
            self._entities[entity.id] = entity
        except LibraryValidatorException as lve:
            print(lve)

    def remove_by_id(self, entity_id):
        """
        Removes an element from the repository, knowing the element's id.
        """
        if self.find_by_id(entity_id) is None:
            raise RepositoryException("Nonexistent id {0}".format(entity_id))
        self._entities.pop(entity_id)

    def get_all(self):
        """
        Returns the list of the values contained in the repository.
        """
        return list(self._entities.values())

    def __len__(self):
        return len(self._entities)

    def __getitem__(self, id):
        return self._entities[id]
