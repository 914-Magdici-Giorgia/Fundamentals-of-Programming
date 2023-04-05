
class Expense:

    def __init__(self,day, amount, type):
        """
        Initialise an expense.
        Each expense has a day (integer between 1 and 30),
        amount of money (positive integer) and expense type (string).
        """
        if day < 1 or day > 30:
            raise ValueError("Day should be an integer number between 1 and 30.")
        if amount < 0:
            raise ValueError ("The amount of money cannot be a negative number.")

        self._day = day
        self._amount = amount
        self._type = type

    @property
    def day (self):
        return self._day

    @property
    def money(self):
        return self._amount

    @property
    def type(self):
        return self._type

    def __str__(self):
        return "Day: " + str(self.day) + "\t\tAmount of money: " + str(self.money) + "\t\tType of expense: " + self.type

    def __eq__(self, other):
        return self.day == other.day and self.money == other.money and self.type == other.type


