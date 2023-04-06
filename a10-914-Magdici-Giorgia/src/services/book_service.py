from src.domain.book import Book
from src.repository.repository import RepositoryException
import random

from src.services.undo import UndoObject
from src.utilities import my_filter


class BookException(Exception):
    pass


class BookService:
    def __init__(self, book_repository, rental_repository, undo_service):
        self.__book_repository = book_repository
        self.__undo_service=undo_service
        self.__rental_repository=rental_repository

    def add_book(self, book_id, author, title):
        """
        Creates a new book with the given data and adds it to the repository.
        """
        new_book = Book(book_id, author, title)
        try:
            self.__book_repository.add(new_book)
            self.__undo_service.register_operation(UndoObject(lambda: self.__book_repository.remove_by_id(new_book.id),
                                                              lambda: self.__book_repository.add(new_book)))
        except RepositoryException as re:
            print(re)

    def add_random_books(self):

        books = {"Hermann Hesse": ["Steppenwolf", "The Glass Bead Game", "Siddhartha"],
                 "F. M. Dostoevsky": ["Notes from Underground", "Crime and Punishment", "The Idiot", "Demons"],
                 "Ernest Hemingway": ["For Whom The Bell Tolls", "The Old Man and the Sea", "The Sun Also Rises",
                                      " A Farewell To Arms"],
                 "Charles Dickens": ["Great Expectations", "Hard Times", "Bleak House", "Oliver Twist"],
                 "Eckhart Tolle": ["The Power of Now", "A New Earth", "Stillness Speaks"],
                 "Jane Austen": ["Pride and Prejudice", "Emma", "Sense and Sensibility", "Persuasion"],
                 "Alexandre Dumas": ["The Count of Monte Cristo", "The Three Musketeers", "La Reine Margot"]}

        authors = list(books.keys())

        for id in range(1, 21):
            random_author = random.choice(authors)
            random_book = random.choice(books[random_author])
            self.add_book(id, random_author, random_book)

    def update_book(self, book_id, author, title):
        """
            Creates a new book with the given data and updates the book from the repository which has the same id with the  new book .
        """
        old_book = self.__book_repository.find_by_id(book_id)
        if not old_book:
            raise BookException("No client with given id")
        new_book = Book(book_id, author, title)
        self.__undo_service.register_operation(
            UndoObject(lambda: self.__book_repository.update(book_id, old_book),
                       lambda: self.__book_repository.update(book_id, new_book)))
        self.__book_repository.update(book_id, new_book)

    def remove_book(self, book_id):
        """
        Removes a book from the repository.
        """
        book = self.__book_repository.find_by_id(book_id)
        if not book:
            raise BookException("No book with given id")
        rentals = list(filter(lambda x: x.book_id == book_id, self.__rental_repository.get_all()))

        def undo_function():
            self.__book_repository.add(book)
            for rental in rentals:
                self.__rental_repository.add(rental)

        def redo_function():
            self.__book_repository.remove_by_id(book.id)
            for rental in rentals:
                self.__rental_repository.remove_by_id(rental.id)

        self.__undo_service.register_operation(UndoObject(undo_function, redo_function))
        self.__book_repository.remove_by_id(book.id)
        for y in [x for x in self.__rental_repository.get_all() if x.book_id == book_id]:
            self.__rental_repository.remove_by_id(y.id)

    def get_all_books(self):
        """
            Returns the list of the values from the book repository.
        """
        return self.__book_repository.get_all()

    def filter_by_id(self, id):
        books = self.__book_repository.get_all()

        # filtered_books = []
        # for book in books:
        #     if id in str(book.id):
        #         filtered_books.append(book)

        filtered_books=my_filter(books, lambda x: id in str(x.id) )
        return filtered_books

    def filter_by_author(self, author):
        books = self.__book_repository.get_all()

        # filtered_books = []
        # for book in books:
        #     if author in book.author.lower():
        #         filtered_books.append(book)

        filtered_books=my_filter(books, lambda x: author in x.author.lower() )

        return filtered_books

    def filter_by_title(self, title):
        books = self.__book_repository.get_all()

        # filtered_books = []
        # for book in books:
        #     if title in book.title.lower():
        #         filtered_books.append(book)
        filtered_books=my_filter(books, lambda x: title in x.title.lower() )

        return filtered_books

    def book_by_id(self,id):
        return self.__book_repository.find_by_id(id)

    def undo(self):
        self.__undo_service.undo()

    def redo(self):
        self.__undo_service.redo()