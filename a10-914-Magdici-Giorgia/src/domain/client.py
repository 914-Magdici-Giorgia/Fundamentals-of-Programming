
class Client:
    """
    This class defines a client and stored its id and its name
    """
    def __init__(self, client_id, name):
        self.__client_id = client_id
        self.__name = name

    @property
    def id(self):
        return self.__client_id

    @id.setter
    def id(self, value):
        self.__client_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return str(self.id) + ", " +str(self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
