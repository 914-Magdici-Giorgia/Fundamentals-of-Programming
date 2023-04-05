from datetime import datetime


class LibraryValidatorException(Exception):
    pass


class BookValidatorException(LibraryValidatorException):
    pass


class ClientValidatorException(LibraryValidatorException):
    pass


class RentalValidatorException(LibraryValidatorException):
    pass

"""
These classes validate the data we try to store in book/client/rental.
"""


class BookValidator:
    @staticmethod
    def validate(book):
        if book.id < 0:
            raise BookValidatorException("The id cannot be negative.")


class ClientValidator:
    @staticmethod
    def validate(client):
        if client.id < 0:
            raise ClientValidatorException("The id cannot be negative.")


class RentalValidator:
    @staticmethod
    def validate(rental):
        #date_format = "%m/%d/%Y"
        rented_date = datetime.strptime(rental.rented_date, "%d/%m/%Y")
        returned_date = datetime.strptime(rental.returned_date, "%d/%m/%Y")
        if rented_date > returned_date:
            raise RentalValidatorException("Invalid period of time")
