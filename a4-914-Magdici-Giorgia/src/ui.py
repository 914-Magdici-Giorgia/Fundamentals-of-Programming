"""
  User interface module
"""

from functions import get_last_list, add_number, set_new_list, insert, remove_pos, \
    remove_interval, replace_nrs, get_real_interval, get_list_mod_comp, sum_interval, \
    product_interval, undo


def add_command_run(hist, param):
    list_nrs = get_last_list(hist).copy()
    param = param.strip()
    add_number(list_nrs, param)
    set_new_list(hist, list_nrs)


def insert_command_run(hist, params):
    list_nrs = get_last_list(hist).copy()
    params = params.strip("., ")
    tokens = params.split()
    if len(tokens) == 3 and tokens[2].isdigit():
        number = tokens[0].lower()
        position = tokens[2]
        try:
            insert(list_nrs, number, position)
            set_new_list(hist, list_nrs)
        except IndexError as ie:
            print(ie)
            return
    else:
        print("Invalid input.")


def remove_command_run(hist, params):
    list_nrs = get_last_list(hist).copy()
    params = params.strip()
    tokens = params.split()
    if len(tokens) == 1 and tokens[0].isdigit():
        position = int(tokens[0])
        try:
            remove_pos(list_nrs, position)
            set_new_list(hist, list_nrs)
        except IndexError as ie:
            print(ie)
            return
    elif len(tokens) == 3 and tokens[0].isdigit() and tokens[2].isdigit():
        start = int(tokens[0])
        end = int(tokens[2])
        try:
            remove_interval(list_nrs, start, end)
            set_new_list(hist, list_nrs)
        except IndexError as ie:
            print(ie)
            return
    else:
        print("Invalid input")


def replace_command_run(hist, params):
    list_nrs = get_last_list(hist).copy()
    params = params.strip()
    tokens = params.split()
    if len(tokens) == 3:
        number1 = tokens[0].lower()
        number2 = tokens[2].lower()
        try:
            replace_nrs(list_nrs, number1, number2)
            set_new_list(hist, list_nrs)
        except ValueError as ve:
            print(ve)
            return
    else:
        print("Invalid input")


def list_command_run(hist, params):
    list_nrs = get_last_list(hist).copy()
    if params is None:
        display(list_nrs)
    else:
        params = params.strip()
        tokens = params.split()
        if len(tokens) == 4 and tokens[1].isdigit() and tokens[3].isdigit():
            start = int(tokens[1])
            end = int(tokens[3])
            try:
                real_in_interval = get_real_interval(list_nrs, start, end)
            except IndexError as ie:
                print(ie)
                return
            display(real_in_interval)
        elif len(tokens) == 3 and tokens[2].isdigit():
            operator = tokens[1]
            number = tokens[2]
            list_modulo = get_list_mod_comp(list_nrs, operator, number)
            display(list_modulo)
        else:
            print("Invalid input")


def sum_command_run(hist, params):
    list_nrs = get_last_list(hist).copy()
    params = params.strip()
    tokens = params.split()
    if len(tokens) == 3 and tokens[0].isdigit() and tokens[2].isdigit():
        start = int(tokens[0])
        end = int(tokens[2])
        try:
            s = sum_interval(list_nrs, start, end)
            print(s)
        except IndexError as ie:
            print(ie)
            return
    else:
        print("Invalid input")


def product_command_run(hist, params):
    list_nrs = get_last_list(hist).copy()
    params = params.strip()
    tokens = params.split()
    if len(tokens) == 3 and tokens[0].isdigit() and tokens[2].isdigit():
        start = int(tokens[0])
        end = int(tokens[2])
        try:
            p = product_interval(list_nrs, start, end)
            print(p)
        except IndexError as ie:
            print(ie)
            return
    else:
        print("Invalid input")


def filter_command_run(hist, params):
    list_nrs = get_last_list(hist).copy()
    params = params.strip()
    tokens = params.split()
    if len(tokens) == 1:
        try:
            list_of_real = get_real_interval(list_nrs, 0, len(list_nrs) - 1)
            list_nrs.clear()
            list_nrs.extend(list_of_real)
            set_new_list(hist, list_nrs)
        except IndexError as ie:
            print(ie)
            return
    elif len(tokens) == 3 and tokens[2].isdigit():
        operator = tokens[1]
        number = tokens[2]
        list_modulo = get_list_mod_comp(list_nrs, operator, number)
        list_nrs.clear()
        list_nrs.extend(list_modulo)
        set_new_list(hist, list_nrs)
    else:
        print("Invalid input")


def undo_command_run(hist, params):
    if params is None:
        try:
            undo(hist)
        except ValueError as ve:
            print(ve)
            return
    else:
        print("Invalid input")


def split_command_params(user_cmd):
    user_cmd = user_cmd.strip()
    tokens = user_cmd.split(maxsplit=1)
    cmd_word = tokens[0].lower() if len(tokens) > 0 else None
    cmd_param = tokens[1].lower() if len(tokens) == 2 else None
    return cmd_word, cmd_param


def display(list_nrs):
    print("\n LIST:", *list_nrs, '\n')


def print_menu():
    print("\n Commands:\n"
          "\tadd <number>\n"
          "\tinsert <number> at <position>\n"
          "\tremove <position>\n"
          "\tremove <start position> to <end position>\n"
          "\treplace <old number> with <new number>\n"
          "\tlist\n"
          "\tlist real <start position> to <end position>\n"
          "\tlist modulo [ < | = | > ] <number>\n"
          "\tsum <start position> to <end position>\n"
          "\tproduct <start position> to <end position>\n"
          "\tfilter real\n"
          "\tfilter modulo [ < | = | > ] <number>\n"
          "\tundo\n"
          "\texit")
