import random
import operator
from datetime import datetime

from src.domain.rental import Rental
import time

from src.repository.repository import RepositoryException

from src.services.undo import UndoObject


class RentalServiceException(Exception):
    pass


class RentalService:
    def __init__(self, rental_repository, book_repository, client_repository, undo_service):
        self.__rental_repository = rental_repository
        self.__book_repository =book_repository
        self.__client_repository=client_repository
        self.__undo_service=undo_service

    def book_is_rented(self, book_id, rented_date, returned_date):
        rented_date = time.strptime(rented_date, "%d/%m/%Y")
        returned_date = time.strptime(returned_date, "%d/%m/%Y")
        rentals = self.get_all_rentals()
        for r in rentals:
            if book_id == r.book_id:
                r_rented = time.strptime(r.rented_date, "%d/%m/%Y")
                r_returned = time.strptime(r.returned_date, "%d/%m/%Y")
                if rented_date < r_rented:
                    if returned_date > r_rented:
                        return True
                elif r_rented < rented_date < r_returned:
                    return True
        return False

    def add_rental(self, rental_id, book_id, client_id, rented_date, returned_date="09/09/9999"):
        new_rental = Rental(rental_id, book_id, client_id, rented_date, returned_date)
        if self.book_is_rented(book_id, rented_date, returned_date) is True:
            raise RentalServiceException("This book is not available in the the requested period")

        try:
            self.__rental_repository.add(new_rental)
            self.__undo_service.register_operation(UndoObject(lambda: self.__rental_repository.remove_by_id(new_rental.id),
                                                              lambda: self.__rental_repository.add(new_rental)))
        except RepositoryException as re:
            print(re)

    def add_random_rentals(self):
        for id in range(1, 51):
            book_id = random.randint(1, 20)
            client_id = random.randint(1, 20)
            random_day = random.randint(1, 28)
            random_month = random.randint(1, 12)
            random_year = random.randint(2015, 2021)
            rent_date = str(random_day) + '/' + str(random_month) + '/' + str(random_year)
            random_day = random.randint(1, 28)
            random_month = random.randint(1, 12)
            random_year = random.randint(2015, 2021)
            return_date = str(random_day) + '/' + str(random_month) + '/' + str(random_year)
            if datetime.strptime(rent_date, "%d/%m/%Y")< datetime.strptime(return_date, "%d/%m/%Y"):
                try:
                    self.add_rental(id, book_id, client_id, rent_date, return_date)
                except RentalServiceException:
                    pass

    def update_rental(self, rental_id, return_date):
        incomplete_rental=self.__rental_repository.find_by_id(rental_id)
        if not incomplete_rental:
            raise RentalServiceException("No rental with given id")
        complete_rental=Rental(incomplete_rental.id,incomplete_rental.book_id, incomplete_rental.client_id, incomplete_rental.rented_date, incomplete_rental.returned_date)
        complete_rental.returned_date=return_date
        try:
            self.__undo_service.register_operation(
                UndoObject(lambda: self.__rental_repository.update(rental_id, incomplete_rental),
                           lambda: self.__rental_repository.update(rental_id, complete_rental)))
            self.__rental_repository.update(rental_id, complete_rental)
        except RepositoryException as re:
                     print(re)


    def remove_rental(self, rental_id):
        try:
            self.__rental_repository.remove_by_id(rental_id)
        except RepositoryException as re:
            print(re)

    def get_all_rentals(self):
        return self.__rental_repository.get_all()

    def books_statistic(self):
        rentals=self.get_all_rentals()
        books=self.__book_repository.get_all()
        rented_books={}

        for book in books:
            number_of_rentals=0
            for rental in rentals:
                if book.id == rental.book_id:
                    number_of_rentals=number_of_rentals+1
            rented_books[book.id]=number_of_rentals

        statistics=dict(sorted(rented_books.items(),key=operator.itemgetter(1), reverse=True))
        return statistics

    def most_rented_books(self):
        statistics=self.books_statistic()
        rented_books={}

        for id in statistics.keys():
            book=self.__book_repository.find_by_id(id)
            rented_books[id]=book

        return rented_books

    def clients_statistics(self):
        rentals = self.get_all_rentals()
        clients = self.__client_repository.get_all()
        active_clients = {}

        for client in clients:
            client_days=0
            for rental in rentals:
                if client.id == rental.client_id:
                    date1=rental.rented_date
                    date2=rental.returned_date
                    date1 = datetime.strptime(date1, "%d/%m/%Y")
                    date2 = datetime.strptime(date2, "%d/%m/%Y")
                    dif = date2 - date1
                    dif=dif.days
                    client_days=client_days+dif
            active_clients[client.id]=client_days

        statistics = dict(sorted(active_clients.items(), key=operator.itemgetter(1), reverse=True))
        #print(statistics)

        return statistics

    def most_active_clients(self):
        statistics=self.clients_statistics()
        active_clients = {}

        for id in statistics.keys():
            client = self.__client_repository.find_by_id(id)
            active_clients[id] = client

        return active_clients

    def author_statistics(self):
        book_statistics=self.books_statistic()
        books=self.__book_repository.get_all()
        rented_authors={}

        for book in books:
            author=book.author
            rented_authors[author]=0

        for id in book_statistics.keys():
            book=self.__book_repository[id]
            rented_authors[book.author]=int(rented_authors[book.author])+int(book_statistics[id])

        statistics = dict(sorted(rented_authors.items(), key=operator.itemgetter(1), reverse=True))
        #print(statistics)
        return statistics

    def rental_by_id(self,id):
        return self.__rental_repository.find_by_id(id)

    def undo(self):
        self.__undo_service.undo()

    def redo(self):
        self.__undo_service.redo()