from src.domain.client import Client

from src.repository.repository import RepositoryException

from src.services.undo import UndoObject
import random

from src.utilities import my_filter


class ClientIdE(Exception):
    pass


class ClientService:
    def __init__(self, client_repository, rental_repository, undo_service):
        self.__client_repository = client_repository
        self.__undo_service=undo_service
        self.__rental_repository = rental_repository

    def add_client(self, client_id, name):
        """
            Creates a new client with the given data and adds it to the repository.
        """
        new_client = Client(client_id, name)
        try:
            self.__client_repository.add(new_client)
            self.__undo_service.register_operation(UndoObject(lambda: self.__client_repository.remove_by_id(new_client.id),
                                                              lambda: self.__client_repository.add(new_client)))
        except RepositoryException as re:
            print(re)

    def add_random_clients(self):
        names = ["Alexandru Mihai", "Andrei Mathe", "Bianca Mereu", "Bogdan Modolea", "Claudia Ioana", "Daria Matei",
                 "Dayana Mardari", "Diana Jugariu", "Andreea Laslo", "Eduard Lupu", "Laura Miron", "Lavinia Ionel",
                 "Marcu Paul", "Matei Sonia", "Paul Moldovan", "Razvan Moga", "Tabita Lucaciu", "Valentina Mihalescu",
                 "Vlad Marti"]
        for id in range(1, 21):
            random_client = random.choice(names)
            self.add_client(id, random_client)

    def update_client(self, client_id, name):
        """
            Creates a new client with the given data and updates the client from the repository which has the same id with the new client .
        """
        old_client = self.__client_repository.find_by_id(client_id)
        if not old_client :
            raise ClientIdE("No client with given id")
        new_client=Client(client_id,name)
        self.__undo_service.register_operation(
            UndoObject(lambda: self.__client_repository.update(client_id, old_client),
                       lambda: self.__client_repository.update(client_id, new_client)))
        self.__client_repository.update(client_id, new_client)

    def remove_client(self, client_id):
        """
            Removes a client from the repository.
        """
        client= self.__client_repository.find_by_id(client_id)
        if not client:
            raise ClientIdE("No client found with the given id.")
        rentals=list(filter(lambda x: x.client_id == client_id, self.__rental_repository.get_all()))

        def undo_function():
            self.__client_repository.add(client)
            for rental in rentals:
                self.__rental_repository.add(rental)

        def redo_function():
            self.__client_repository.remove_by_id(client.id)
            for rental in rentals:
                self.__rental_repository.remove_by_id(rental.id)

        self.__undo_service.register_operation(UndoObject(undo_function,redo_function))
        self.__client_repository.remove_by_id(client.id)
        for y in [x for x in self.__rental_repository.get_all() if x.client_id==client_id]:
            self.__rental_repository.remove_by_id(y.id)


    def get_all_clients(self):
        """
            Returns the list of the values from the client repository.
        """
        return self.__client_repository.get_all()

    def filter_by_id(self, id):
        clients = self.__client_repository.get_all()

        # filtered_clients = []
        # for client in clients:
        #     if id in str(client.id):
        #         filtered_clients.append(client)

        filtered_clients=my_filter(clients, lambda x: id in str(x.id) )

        return filtered_clients

    def filter_by_name(self, name):
        clients = self.__client_repository.get_all()

        # filtered_clients = []
        # for client in clients:
        #     if name in client.name.lower():
        #         filtered_clients.append(client)
        filtered_clients=my_filter(clients, lambda x: name in x.name.lower() )

        return filtered_clients

    def client_by_id(self,id):
        return self.__client_repository.find_by_id(id)

    def undo(self):
        self.__undo_service.undo()

    def redo(self):
        self.__undo_service.redo()