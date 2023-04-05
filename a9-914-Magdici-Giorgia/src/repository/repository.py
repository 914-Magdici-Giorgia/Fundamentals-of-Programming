import pickle

from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
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

class BookTextFileRepository (Repository):
    def __init__(self,validator_class, file_name):
        super().__init__(validator_class)

        self._file_name =file_name
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, 'rt')
        for line in f.readlines():
            id, author, title=line.split(', ',2)
            self.add(Book(int(id), author, title.rstrip()))

        f.close()

    def _save_file(self):
        f = open(self._file_name, 'wt')

        for book in self._entities.values():
            f.write(str(book)+'\n')
        f.close()


    def add(self, entity):
        super(BookTextFileRepository, self).add(entity)
        self._save_file()

    def update(self, entity_id, entity):
        super(BookTextFileRepository, self).update(entity_id, entity)
        self._save_file()

    def remove_by_id(self, entity_id):
        super(BookTextFileRepository, self).remove_by_id(entity_id)
        self._save_file()


class BookBinFileRepository (Repository):
    def __init__(self,validator_class,file_name):
        super().__init__(validator_class)

        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, 'rb')
        self._entities = pickle.load(f)

        f.close()

    def _save_file(self):
        f = open(self._file_name, 'wb')
        pickle.dump(self._entities, f)
        f.close()


    def add(self, entity):
        super(BookBinFileRepository, self).add(entity)
        self._save_file()

    def update(self, entity_id, entity):
        super(BookBinFileRepository, self).update(entity_id, entity)
        self._save_file()

    def remove_by_id(self, entity_id):
        super(BookBinFileRepository, self).remove_by_id(entity_id)
        self._save_file()


class ClientTextFileRepository (Repository):
    def __init__(self,validator_class,file_name):
        super().__init__(validator_class)

        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, 'rt')
        for line in f.readlines():
            id, name=line.split(', ',1)
            self.add(Client(int(id), name.rstrip()))

        f.close()

    def _save_file(self):
        f = open(self._file_name, 'wt')

        for client in self._entities.values():
            f.write(str(client)+'\n')
        f.close()


    def add(self, entity):
        super(ClientTextFileRepository, self).add(entity)
        self._save_file()

    def update(self, entity_id, entity):
        super(ClientTextFileRepository, self).update(entity_id, entity)
        self._save_file()

    def remove_by_id(self, entity_id):
        super(ClientTextFileRepository, self).remove_by_id(entity_id)
        self._save_file()


class ClientBinFileRepository (Repository):
    def __init__(self,validator_class, file_name):
        super().__init__(validator_class)

        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, 'rb')
        self._entities = pickle.load(f)

        f.close()

    def _save_file(self):
        f = open(self._file_name, 'wb')
        pickle.dump(self._entities, f)

        f.close()

    def add(self, entity):
        super(ClientBinFileRepository, self).add(entity)
        self._save_file()

    def update(self, entity_id, entity):
        super(ClientBinFileRepository, self).update(entity_id, entity)
        self._save_file()

    def remove_by_id(self, entity_id):
        super(ClientBinFileRepository, self).remove_by_id(entity_id)
        self._save_file()



class RentalTextFileRepository (Repository):
    def __init__(self,validator_class,file_name):
        super().__init__(validator_class)

        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, 'rt')
        for line in f.readlines():
            id,  id_book, id_client,date1, date2=line.split(', ')
            self.add(Rental(int(id),int(id_book), int(id_client),date1, date2.rstrip()))

        f.close()

    def _save_file(self):
        f = open(self._file_name, 'wt')

        for rental in self._entities.values():
            f.write(str(rental)+'\n')
        f.close()


    def add(self, entity):
        super(RentalTextFileRepository, self).add(entity)
        self._save_file()

    def update(self, entity_id, entity):
        super(RentalTextFileRepository, self).update(entity_id, entity)
        self._save_file()

    def remove_by_id(self, entity_id):
        super(RentalTextFileRepository, self).remove_by_id(entity_id)
        self._save_file()

class RentalBinFileRepository (Repository):
    def __init__(self,validator_class,file_name):
        super().__init__(validator_class)

        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, 'rb')
        self._entities = pickle.load(f)

        f.close()

    def _save_file(self):
        f = open(self._file_name, 'wb')
        pickle.dump(self._entities, f)

        f.close()


    def add(self, entity):
        super(RentalBinFileRepository, self).add(entity)
        self._save_file()

    def update(self, entity_id, entity):
        super(RentalBinFileRepository, self).update(entity_id, entity)
        self._save_file()

    def remove_by_id(self, entity_id):
        super(RentalBinFileRepository, self).remove_by_id(entity_id)
        self._save_file()

