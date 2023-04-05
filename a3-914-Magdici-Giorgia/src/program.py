"""
  Write non-UI functions below
"""
"""
    1. Numerical List
    A math teacher needs a program to help students test different properties of complex numbers, provided in the a+bi
    form (we assume a and b are integers for simplicity).
    Write a program that implements the functionalities exemplified below:

    (A) Add a number
    add <number>
    insert <number> at <position>
    e.g.
    add 4+2i – appends 4+2i to the list
    insert 1+1i at 1 – insert number 1+i at position 1 in the list (positions are numbered starting from 0)

    (B) Modify numbers
    remove <position>
    remove <start position> to <end position>
    replace <old number> with <new number>
    e.g.
    remove 1 – removes the number at position 1
    remove 1 to 3 – removes the numbers at positions 1,2, and 3
    replace 1+3i with 5-3i – replaces all occurrences of number 1+3i with the number 5-3i

    (C) Display numbers having different properties
    list
    list real <start position> to <end position>
    list modulo [ < | = | > ] <number>
    e.g.
    list – display the list of numbers
    list real 1 to 5 – display the real numbers (imaginary part =0) between positions 1 and 5
    list modulo < 10 – display all numbers having modulo <10
    list modulo = 5 – display all numbers having modulo =5

"""

import math


def set_complex(list_nrs, index, complex):
    list_nrs[index]=complex


def get_complex(list_nrs, index):
    return list_nrs[index]


def get_coefficients(complex):
    """
    the function returns a list with the coefficients of the complex number a+bi
    :param complex: a complex number, in the a+bi form
    :return: [a,b]
    """
    complex = complex.strip("+ ")
    flagi = complex.find("i")
    if flagi == -1:
        real = complex
        imaginary = 0
    elif flagi == 0:
        real = 0
        imaginary = 1
    elif flagi == 1 and complex[0] == '-':
        real = 0
        imaginary = -1
    else:
        coef = complex.split('+', 1)
        if len(coef) == 2:
            real = coef[0]
            if coef[1]== 'i':
                imaginary=1
            else:
                imaginary = coef[1].strip("i ")
        else:
            if coef[0].find("-") != -1:
                coef = coef[0].rsplit("-", 1)
                if len(coef) == 2:
                    if coef[0] == '':
                        real = 0
                    else:
                        real = coef[0]
                    if coef[1]== 'i':
                        imaginary= -1
                    else:
                        imaginary = coef[1].strip("i ")
                        imaginary = int(imaginary)
                        imaginary = -imaginary
                else:
                    real = 0
                    imaginary = coef[0].strip('i ')
            else:
                real = 0
                imaginary = coef[0].strip('i ')
    real = int(real)
    imaginary = int(imaginary)
    return [real, imaginary]



def get_real(complex):
    return get_coefficients(complex)[0]


def get_imaginary(complex):
    return get_coefficients(complex)[1]


def add_number(list_nrs, complex):
    """
    adds a complex number to the list
    :param list_nrs: the list of complex numbers
    :param complex: a+bi which will be added to the list
    :return: the modified list
    """
    list_nrs.append(complex)
    return list_nrs



def insert(list_nrs, complex, pos):
    """
    inserts a complex number in the list
    :param list_nrs: list of complex numbers
    :param complex: the new complex number a+bi
    :param pos: the position where the new number will be inserted
    :return the modified list
    """
    pos=int(pos)
    if pos < 0 or pos > len(list_nrs):
        raise IndexError("Invalid position")
    list_nrs.insert(pos, complex)
    return list_nrs



def remove_pos(list_nrs, pos):
    """
    removes the number from the position pos
    :param list_nrs: list of complex numbers
    :param pos: the removed position
    :return: the list modified
    """
    if pos<0 or pos>len(list_nrs)-1:
        raise IndexError("Invalid position")
    list_nrs.pop(pos)
    return list_nrs



def remove_interval(list_nrs, start, end):
    """
    removes an interval from the list
    :param list_nrs: list of complex numbers
    :param start: starting position of the removed interval
    :param end: the ending position  of the interval
    :return: the list modified
    """
    if start < 0 or start> len(list_nrs) -1 or end < 0 or end > len(list_nrs) - 1 or start>=end:
        raise IndexError("This interval does not exist")
    del list_nrs[start:end + 1]
    return list_nrs



def replace_nrs(list_nrs, complex1, complex2):
    """
    replaces a complex number from the list with another one
    :param list_nrs: list of complex numbers
    :param complex1: the replaced number
    :param complex2: the number that replaced the other one
    :return: the modified list
    """
    count=list_nrs.count(complex1)
    if count > 0:
        for index, complex in enumerate(list_nrs):
            if complex == complex1:
                set_complex(list_nrs, index, complex2)
        return list_nrs
    else:
        raise ValueError("This number is not in your list.")

def display_real_interval(list_nrs, start, end):
    """
    returns the real numbers (imaginary part =0) between positions start and end from the list
    :param list_nrs:list of complex numbers
    :param start: starting position of the interval
    :param end:ending position of the interval
    :return:a new list formed with found values
    """
    interval = list_nrs[start:end + 1]
    list_real=[]
    if start < 0 or start> len(list_nrs) -1 or end < 0 or end > len(list_nrs) - 1 or start>end:
        raise IndexError("Invalid position")
    for complex in interval:
        if get_imaginary(complex) == 0:
            list_real.append(complex)
    return list_real

def modulo(complex):
    """
    calculates the modulo of a complex number
    :param complex: a+bi
    :return: sqrt(a*a+b*b)
    """
    re = get_real(complex)
    im = get_imaginary(complex)
    result = math.sqrt(re * re + im * im)
    return result


def display_mod_comp(list_nrs, operator, number):
    """
    returns all numbers having requested modulo
    :param list_nrs: list of complex numbers
    :param comp: [ < | = | > ] <number>
    :return:a new list with found numbers
    """

    number = int(number)
    new_list=[]
    if operator == '>':
        for complex in list_nrs:
            if modulo(complex) > number:
                new_list.append(complex)
    elif operator == '=':
        for complex in list_nrs:
            if modulo(complex) == number:
                new_list.append(complex)
    elif operator == '<':
        for complex in list_nrs:
            if modulo(complex) < number:
                new_list.append(complex)
    else:
        print("invalid input")
    return new_list



def test_get_coefficients():
    assert get_coefficients("+3+7i") == [3, 7]
    assert get_coefficients("3-i") == [3,-1]
    assert get_coefficients("+3") == [3, 0]
    assert get_coefficients("+7i") == [0, 7]
    assert get_coefficients("+i") == [0, 1]
    assert get_coefficients("+3-7i") == [3, -7]
    assert get_coefficients("-3+7i") == [-3, 7]
    assert get_coefficients("3") == [3, 0]
    assert get_coefficients("7i") == [0, 7]
    assert get_coefficients("i") == [0, 1]
    assert get_coefficients("3-7i") == [3, -7]
    assert get_coefficients("-3") == [-3, 0]
    assert get_coefficients("-7i") == [0, -7]
    assert get_coefficients("-i") == [0, -1]
    assert get_coefficients("-3-7i") == [-3, -7]

test_get_coefficients()

def test_add_number():
    assert add_number([], "6+9i")==["6+9i"]
    assert add_number(["3", "8i", "2+4i"], "i")==["3", "8i", "2+4i", "i"]

test_add_number()

def test_insert():
    assert insert([],"3", 0)==["3"]
    assert insert(["2+8i","2+4i","6+9i"],"5+87i",2)==["2+8i","2+4i","5+87i","6+9i"]

test_insert()

def test_insert():
    assert insert([],"3", 0)==["3"]
    assert insert(["2+8i","2+4i","6+9i"],"5+87i",2)==["2+8i","2+4i","5+87i","6+9i"]

test_insert()

def test_remove_pos():
    assert remove_pos(["2+8i","2+4i","5+87i","6+9i"], 2)==["2+8i","2+4i","6+9i"]
    assert remove_pos(["1+3i", "6+i", "87i", "12+5i"], 0) == ["6+i", "87i", "12+5i"]

test_remove_pos()

def test_remove_interval():
    assert remove_interval(["2+8i","2+4i","5+87i","6+9i"],0,2 )==["6+9i"]
    assert remove_interval(["2+8i", "2+4i", "5+87i", "6+9i"], 0, 3)==[]
    assert remove_interval(["2+8i", "2+4i", "5+87i", "6+9i"], 2,3)==["2+8i", "2+4i"]

test_remove_interval()

def test_replace_nrs():
    assert replace_nrs(["2+8i","2i","2+4i","2i","5+87i","6+9i"],"2i", "5i" )==["2+8i","5i","2+4i","5i","5+87i","6+9i"]
    assert replace_nrs(["2+8i", "4i", "2+4i", "6i", "5+87i", "2+4i"], "2+4i", "5+7i")==["2+8i", "4i", "5+7i", "6i", "5+87i", "5+7i"]

test_replace_nrs()

def test_display_real_interval():
    assert display_real_interval(["2+8i", "4", "2", "6i", "5", "2+4i", "2+4i", "5+7i"],0,4)==["4","2", "5"]
    assert display_real_interval(["2+8i", "4i", "2+4i", "6", "5+87i", "2+4i", "2+4i", "5"],3,7)==["6", "5"]

test_display_real_interval()

def test_modulo():
    assert modulo("3+4i")==5
    assert modulo("6")==6
    assert modulo("9i")==9
    assert modulo("i")==1
    assert modulo("0")==0

test_modulo()

def test_display_mod_comp():
    assert display_mod_comp(["2+8i", "4i", "2+4i", "6", "5+87i", "2+4i", "2+4i", "5"],">","5")==["2+8i", "6", "5+87i"]
    assert display_mod_comp(["2+8i", "5i", "3+4i", "6", "5+87i", "3+4i", "2+4i", "5"], "=","5")==["5i", "3+4i", "3+4i", "5"]
    assert display_mod_comp(["2+8i", "4i", "1+4i", "6", "2i", "8+4i", "2+4i", "3"], "<","5")==["4i", "1+4i","2i","2+4i", "3"]

test_display_mod_comp()



"""
  Write the command-driven UI below
"""

def add_command_run(list_nrs, param):
    param=param.strip()
    add_number(list_nrs,param)


def insert_command_run(list_nrs, params):
    params=params.strip("., ")
    tokens= params.split()
    if len(tokens) == 3 and tokens[2].isdigit():
        number = tokens[0].lower()
        position = tokens[2]
        try:
            insert(list_nrs, number, position)
        except IndexError as ie:
            print(ie)
            return
    else:
        print("Invalid input.")



def remove_command_run(list_nrs, params):

    params=params.strip()
    tokens=params.split()
    if len(tokens)==1 and tokens[0].isdigit():
        position=int(tokens[0])
        try:
            remove_pos(list_nrs, position)
        except IndexError as ie:
            print(ie)
            return
    elif len(tokens) == 3 and tokens[0].isdigit() and tokens[2].isdigit():
        start=int(tokens[0])
        end=int(tokens[2])
        try:
            remove_interval(list_nrs, start, end)
        except IndexError as ie:
            print(ie)
            return
    else:
        print("Invalid input")



def replace_command_run(list_nrs, params):
    params = params.strip()
    tokens = params.split()
    if len(tokens)==3:
        number1=tokens[0].lower()
        number2=tokens[2].lower()
        try:
            replace_nrs(list_nrs, number1, number2)
        except ValueError as ve:
            print(ve)
            return
    else:
        print("Invalid input")


def list_command_run(list_nrs, params):

    if params is None:
        display(list_nrs)
    else:
        params = params.strip()
        tokens = params.split()
        if len(tokens) == 4 and tokens[1].isdigit() and tokens[3].isdigit():
            start=int(tokens[1])
            end=int(tokens[3])
            try:
                real_in_interval = display_real_interval(list_nrs, start, end)
            except IndexError as ie:
                print(ie)
                return
            display(real_in_interval)
        elif len(tokens)== 3 and tokens[2].isdigit():
            operator= tokens[1]
            number=tokens[2]
            list_modulo=display_mod_comp(list_nrs, operator, number)
            display(list_modulo)
        else:
            print ("Invalid input")

def split_command_params(user_cmd):
    user_cmd = user_cmd.strip()
    tokens = user_cmd.split(maxsplit=1)
    cmd_word = tokens[0].lower() if len(tokens) > 0 else None
    cmd_param = tokens[1].lower() if len(tokens) == 2 else None
    return cmd_word, cmd_param


def display(list):
    print("\n LIST:",*list, '\n')


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
          "\texit" )




def start_command_ui():
    list_nrs = ['1+3i', '2', '5i', '2i', '5', '12+i', '3+6i']
    commands = {'add': add_command_run,
                'insert': insert_command_run,
                'remove': remove_command_run,
                'replace': replace_command_run,
                'list': list_command_run
                }
    while True:
        print_menu()
        user_cmd=input("Insert you command:")
        cmd_word, cmd_params = split_command_params(user_cmd)

        if cmd_word == 'exit':
            return

        if cmd_word not in commands:
            print("Invalid command")
        else:
            commands[cmd_word](list_nrs, cmd_params)


start_command_ui()