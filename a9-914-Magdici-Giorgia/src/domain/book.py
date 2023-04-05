class Book:
    """
    This class defines a book and stores its id, author and title
    """

    def __init__(self, book_id, author, title):
        self.__book_id = book_id
        self.__title = title
        self.__author = author

    @property
    def id(self):
        return self.__book_id

    @id.setter
    def id(self, value):
        self.__book_id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    def __str__(self):
        return str(self.id) + ", " + str(self.author) + ", " + str(self.title)

    def __eq__(self, other):
        return self.id == other.id and self.author == other.author and self.title == other.title