from src.domain.book import Book
from src.domain.validators import BookValidator, ClientValidator, RentalValidator
from src.repository.repository import Repository
from src.services.book_service import BookService
from src.services.client_service import ClientService
from src.services.rental_service import RentalService, RentalServiceException

from datetime import datetime

from src.services.undo import UndoService, UndoBounds


class Console:
    def __init__(self, book_service, client_service, rental_service, undo_service):
        self.__book_service = book_service
        self.__client_service = client_service
        self.__rental_service = rental_service
        self.__undo_service=undo_service

    def run_console(self):
        self.__book_service.add_random_books()
        self.__client_service.add_random_clients()
        self.__rental_service.add_random_rentals()
        #self.__print_all_books()

        commands = {'1': self.__add_book,
                    '2': self.__add_client,
                    '3': self.__update_book,
                    '4': self.__update_client,
                    '5': self.__remove_book,
                    '6': self.__remove_client,
                    '7': self.__print_all_books,
                    '8': self.__print_all_clients,
                    '9': self.__rent_book,
                    '10': self.__return_book,
                    '11': self.__print_all_rentals,
                    '12': self.__search_book,
                    '13': self.__search_client,
                    '14': self.__most_rented_books,
                    '15': self.__most_active_clients,
                    '16': self.__most_rented_author,
                    '17': self.__undo,
                    '18':self.__redo
                    }

        while True:
            self.print_menu()
            _command = input("Command:").strip().lower()
            if _command == 'x':
                return
            elif _command not in commands:
                print("Invalid command!")
            else:
                try:
                    commands[_command]()
                except ValueError as ve:
                    print("ERROR - " + str(ve))







    def print_menu(self):
        print("Menu:")
        print("\t1 - add book\n\t2 - add client\n\t3 - update book\n\t4 - update client\n\t5 - remove book\n\t6 - "
              "remove client\n\t7 - list books\n\t8 - list clients\n\t9 - rent book\n\t10 - return book\n\t11 - list "
              "rentals\n\t12 - search book\n\t13 - search client\n\t14 - most rented books\n\t15 - most active "
              "clients\n\t16 - most rented authors\n\t17 - undo\n\t18 - redo")

    def __print_all_books(self):
        books = self.__book_service.get_all_books()
        self.__print_list(books)

    def __print_all_clients(self):
        clients = self.__client_service.get_all_clients()
        self.__print_list(clients)

    def __print_all_rentals(self):
        rentals = self.__rental_service.get_all_rentals()
        self.__print_list(rentals)

    def __print_list(self, lists):
        for e in lists:
            print(e)

    def __add_book(self):
        print("For adding a book, please enter its")
        id = int(input("id:"))
        author = input("author:")
        title = input("title:")
        self.__book_service.add_book(id, author, title)


    def __add_client(self):
        print("For adding a client, please enter its")
        id = int(input("id:"))
        name = input("name:")
        self.__client_service.add_client(id, name)

    def __rent_book(self):
        print("For renting a book, please enter")
        rental_id = int(input("rental id:"))
        book_id = int(input("book id:"))
        client_id = int(input("client id:"))
        rented_date = input("and the rent date (dd/mm/yyy):")
        try:
            self.__rental_service.add_rental(rental_id, book_id, client_id, rented_date)
        except RentalServiceException as rse:
            print(rse)

    def __return_book(self):
        print("For returning a book, please enter")
        rental_id = int(input("rental id:"))
        return_date=input("add return date(dd/mm/yyyy):")
        self.__rental_service.update_rental(rental_id, return_date)

    def __update_book(self):
        print("For updating a book, please enter its")
        id = int(input("id:"))
        author = input("updated author:")
        title = input("updated title:")
        self.__book_service.update_book(id, author, title)

    def __update_client(self):
        print("For updating a client, please enter its")
        id = int(input("id:"))
        name = input(" updated name:")
        self.__client_service.update_client(id, name)

    def __remove_book(self):
        print("For removing a book, please enter its")
        id = int(input("id:"))
        self.__book_service.remove_book(id)

    def __remove_client(self):
        print("For removing a client, please enter its")
        id = int(input("id:"))
        self.__client_service.remove_client(id)

    def __search_book(self):
        field = input("search by:\n\ta id\n\tb author\n\tc title\n")
        field = field.lower().strip()
        search = input("search for:")
        search = search.lower().strip()
        if field == "a":
            filtered_list = self.__book_service.filter_by_id(search)
        elif field == "b":
            filtered_list = self.__book_service.filter_by_author(search)
        elif field == "c":
            filtered_list = self.__book_service.filter_by_title(search)
        else:
            print("Invalid field")

        self.__print_list(filtered_list)

    def __search_client(self):
        field = input("search by:\n\ta id\n\tb name\n ")
        field = field.lower().strip()
        search = input("search for:")
        search = search.lower().strip()
        if field == "a":
            filtered_list = self.__client_service.filter_by_id(search)
        elif field == "b":
            filtered_list = self.__client_service.filter_by_name(search)
        else:
            print("Invalid field")

        self.__print_list(filtered_list)

    def __most_rented_books(self):
        rented_books = self.__rental_service.most_rented_books()
        for book in rented_books.values():
            print(book)

    def __most_active_clients(self):
        active_clients = self.__rental_service.most_active_clients()
        for client in active_clients.values():
            print(client)

    def __most_rented_author(self):
        rented_authors = self.__rental_service.author_statistics()
        for author in rented_authors:
            print(author)

    def __undo(self):
        try:
            self.__undo_service.undo()
        except UndoBounds as ub:
             print(ub)


    def __redo(self):
        try:
            self.__undo_service.redo()
        except UndoBounds as ub:
            print(ub)



book_validator = BookValidator
client_validator = ClientValidator
rental_validator = RentalValidator

book_repo = Repository(book_validator)
client_repo = Repository(client_validator)
rental_repo = Repository(rental_validator)


undo_service = UndoService(book_repo, client_repo, rental_repo)
book_service = BookService(book_repo,rental_repo, undo_service)
client_service = ClientService(client_repo, rental_repo, undo_service)
rental_service = RentalService(rental_repo, book_repo, client_repo, undo_service)

console = Console(book_service, client_service, rental_service, undo_service)
console.run_console()
