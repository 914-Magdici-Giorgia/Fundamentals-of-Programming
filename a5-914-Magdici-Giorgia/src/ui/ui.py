from services.services import List_of_expenses


class UI:
    def __init__(self, Data):
        self._commands = {'add': self.add_expense,
                          'list': self.display,
                          'filter': self.filter,
                          'undo': self.undo
                          }
        self._data = Data


    def _print_menu(self):
        print("Menu:")
        print("     'add' for adding an expense to your list")
        print("     'list' to display your list of expenses")
        print("     'filter' to filter the list and obtain only the expenses above a certain value")
        print("     'undo' to undo an operation that modified your list")
        print("     'x' to close the menu")

    def add_expense(self):
        day=int(input("In which day?  "))
        amount=int(input("How much?  "))
        type=input("On what?")

        self._data.add_expense(day,amount,type)

    def display(self):
        self._data.print_list()

    def filter(self):
        value=int(input("Value: "))
        self._list=self._data.filter(value)

    def undo(self):
        self._data.undo()


    def start(self):
        while True:
            self._print_menu()
            _command = input("Command:").strip().lower()
            if _command=='x':
                return
            elif _command not in self._commands:
                print("Invalid command!")
            else:
                try:
                    self._commands[_command]()
                except ValueError as ve:
                    print("ERROR - " + str(ve))



Data_Expenses= List_of_expenses()
Data_Expenses.get_random_list()
ui=UI(Data_Expenses)
ui.start()

