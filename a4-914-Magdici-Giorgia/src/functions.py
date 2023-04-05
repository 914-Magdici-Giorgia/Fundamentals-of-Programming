"""
  Program functionalities module
"""

import math


def set_complex(list_nrs, index, complex):
    list_nrs[index] = complex


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
            if coef[1] == 'i':
                imaginary = 1
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
                    if coef[1] == 'i':
                        imaginary = -1
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


def get_str(complex):
    """

    :param complex: [a,b]
    :return:
    """
    a = complex[0]
    b = complex[1]
    if a != 0:
        if b > 1:
            return str(a) + "+" + str(b) + "i"
        elif b == 1:
            return str(a) + "+" + "i"
        elif b == -1:
            return str(a) + "-" + "i"
        elif b < -1:
            return str(a) + str(b) + "i"
        else:
            return str(a)
    else:
        if b != 0:
            return str(b) + "i"
        else:
            return str(a)


def is_real(complex):
    if get_imaginary(complex) == 0:
        return True
    else:
        return False


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
    pos = int(pos)
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
    if pos < 0 or pos > len(list_nrs) - 1:
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
    if start < 0 or start > len(list_nrs) - 1 or end < 0 or end > len(list_nrs) - 1 or start >= end:
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
    count = list_nrs.count(complex1)
    if count > 0:
        for index, complex in enumerate(list_nrs):
            if complex == complex1:
                set_complex(list_nrs, index, complex2)
        return list_nrs
    else:
        raise ValueError("This number is not in your list.")


def get_real_interval(list_nrs, start, end):
    """
    returns the real numbers (imaginary part =0) between positions start and end from the list
    :param list_nrs:list of complex numbers
    :param start: starting position of the interval
    :param end:ending position of the interval
    :return:a new list formed with found values
    """
    interval = list_nrs[start:end + 1]
    list_real = []
    if start < 0 or start > len(list_nrs) - 1 or end < 0 or end > len(list_nrs) - 1 or start > end:
        raise IndexError("Invalid position")
    for complex in interval:
        if is_real(complex) is True:
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


def get_list_mod_comp(list_nrs, operator, number):
    """
    returns all numbers having requested modulo
    :param list_nrs: list of complex numbers
    :param comp: [ < | = | > ] <number>
    :return:a new list with found numbers
    """

    number = int(number)
    new_list = []
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


def sum_complex(complex1, complex2):
    """
    The sum of 2 complex numbers
    :param complex1: [a1, b1]
    :param complex2: [a2,b2]
    :return: [a1+a2,b1+b2]
    """
    s = []
    a1 = get_real(complex1)
    b1 = get_imaginary(complex1)
    a2 = get_real(complex2)
    b2 = get_imaginary(complex2)

    s.append(a1 + a2)
    s.append(b1 + b2)
    return get_str(s)


def sum_interval(list_nrs, start, end):
    """
    This function calculates the sum of all complex numbers located between positions 'start' and 'end'.
    :param list_nrs: list of complex numbers
    :param start: the starting position of the interval
    :param end: the ending position of the interval
    :return:the result
    """
    if start < 0 or start > len(list_nrs) - 1 or end < 0 or end > len(list_nrs) - 1 or start > end:
        raise IndexError("This interval does not exist")

    if start == end:
        return get_complex(list_nrs, start)

    result = get_complex(list_nrs, start)
    for index in range(start + 1, end + 1):
        complex = get_complex(list_nrs, index)
        result = sum_complex(result, complex)

    return result


def prod_complex(complex1, complex2):
    """
    The product between 2 complex numbers.
    :param complex1: [a1,b1]
    :param complex2: [a2,b2]
    :return: the result [pa,pb]=(a1*a2-b1*b2)+(a1*b2+a2*b1)i
    """
    p = []
    a1 = get_real(complex1)
    b1 = get_imaginary(complex1)
    a2 = get_real(complex2)
    b2 = get_imaginary(complex2)
    pa = a1 * a2 - b1 * b2
    pb = a1 * b2 + a2 * b1
    p.append(pa)
    p.append(pb)
    return get_str(p)


def product_interval(list_nrs, start, end):
    """
    This function calculates the product of all complex numbers located between positions 'start' and 'end'.
    :param list_nrs: list of complex numbers
    :param start: the starting position of the interval
    :param end: the ending position of the interval
    :return:the result
    """
    if start < 0 or start > len(list_nrs) - 1 or end < 0 or end > len(list_nrs) - 1 or start > end:
        raise IndexError("This interval does not exist")

    if start == end:
        return get_complex(list_nrs, start)

    result = get_complex(list_nrs, start)
    for index in range(start + 1, end + 1):
        complex = get_complex(list_nrs, index)
        result = prod_complex(result, complex)

    return result


def init_history():
    return [['1+3i', '2', '5i', '2i', '5', '12+i', '3+6i']]


def get_last_list(hist):
    return hist[-1]


def set_new_list(hist, list_nrs):
    hist.append(list_nrs)


def undo(hist):
    if len(hist) == 1:
        raise ValueError("You have nothing to undo.")
    hist.pop()
