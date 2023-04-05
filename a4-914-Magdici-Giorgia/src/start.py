"""
  Start the program by running this module
"""

from ui import split_command_params, add_command_run, insert_command_run, \
    remove_command_run, replace_command_run, list_command_run, sum_command_run, \
    product_command_run, filter_command_run, undo_command_run
from functions import init_history
from tests import test_functions


def start_command_ui():
    hist = init_history()
    commands = {'add': add_command_run,
                'insert': insert_command_run,
                'remove': remove_command_run,
                'replace': replace_command_run,
                'list': list_command_run,
                'sum': sum_command_run,
                'product': product_command_run,
                'filter': filter_command_run,
                'undo': undo_command_run
                }
    while True:
        # print_menu()
        user_cmd = input("Insert you command:")
        cmd_word, cmd_params = split_command_params(user_cmd)

        if cmd_word == 'exit':
            return

        if cmd_word not in commands:
            print("Invalid command")
        else:
            commands[cmd_word](hist, cmd_params)


start_command_ui()
test_functions()
