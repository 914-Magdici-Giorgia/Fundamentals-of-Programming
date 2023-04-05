from domain.domain import Expense
import random


class List_of_expenses:
    def __init__(self):
        self._list = []
        self._history = []
        self._len = 0
        self._lenh=[]

    @property
    def list(self):
        return self._list

    def get_expense(self, index):
        return self._list[index]

    def add(self, day, amount, type):
        """
        The function adds an expense to the list
        """
        new_expense = Expense(day, amount, type)
        self._list.append(new_expense)
        self._len += 1

    def add_expense(self, day, amount, type):
        """
        The function adds an expense to the list and saves the changed list in the history.

        """
        self._history.append(self._list)
        self._lenh.append(self._len)
        self.add(day, amount, type)

    def get_random_list(self):
        """
        Generating a random list of 10 expenses.
        """
        for i in range(10):
            random_day = random.randrange(1, 31)
            random_amount = random.randrange(100, 1000)
            types = ['food', 'clothes', 'groceries', 'groceries','sneakers', 'bills', 'bills','skincare']
            random_type = random.choice(types)
            self.add(random_day, random_amount, random_type)

    def print_list(self):
        for index in range(self._len):
            print(str(self.get_expense(index)))

    def filter(self, value):
        self._history.append(self._list)
        self._lenh.append(self._len)
        copy_list = self._list
        self._list = []
        self._len = 0

        for expense in copy_list:
            if expense.money > value:
                self.add(expense.day, expense.money, expense.type)
        return self._list

    def pop_history(self):
        return self._history.pop()

    def undo(self):
        if len(self._lenh) == 0:
            raise ValueError('No more undo steps!')
        self._list = self.pop_history()
        self._len =self._lenh.pop()


def test_add_expense():
    data=List_of_expenses()
    data.add_expense(17,266,'bills')
    ex=Expense(17,266,'bills')
    assert data.get_expense(0) == ex
    data.add_expense(3, 56, 'food')
    ex = Expense(3, 56, 'food')
    assert data.get_expense(1) == ex
    data.add_expense(8, 100, 'gift')
    ex = Expense(8, 100, 'gift')
    assert data.get_expense(2) == ex
    data.add_expense(20, 90, 'groceries')
    ex = Expense(20, 90, 'groceries')
    assert data.get_expense(3) == ex

test_add_expense()