
class Rental:
    def __init__(self, rental_id, book_id, client_id, rented_date, returned_date):
        self.__rental_id = rental_id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__returned_date = returned_date

    @property
    def id(self):
        return self.__rental_id

    @id.setter
    def id(self, value):
        self.__rental_id = value

    @property
    def book_id(self):
        return self.__book_id

    @book_id.setter
    def book_id(self, value):
        self.__book_id = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = value

    @property
    def rented_date(self):
        return self.__rented_date

    @rented_date.setter
    def rented_date(self, value):
        self.__rented_date = value

    @property
    def returned_date(self):
        return self.__returned_date

    @returned_date.setter
    def returned_date(self, value):
        self.__returned_date = value

    def __str__(self):
        string=str(self.id)+", "+str(self.book_id)+", "+str(self.client_id)+", "+str(self.rented_date)+", "
        if self.returned_date=='09/09/9999':
            string=string+"still rented"
        else:
            string=string+str(self.returned_date)
        return string

    def __eq__(self, other):
        return self.id==other.id and self.client_id==other.client_id and self.book_id==other.book_id and self.rented_date==other.rented_date and self.returned_date==other.returned_date