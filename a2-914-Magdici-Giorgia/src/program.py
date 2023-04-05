#
# Write the implementation for A2 in this file
#
'''
Implement a menu-driven console application that provides the following functionalities:

    1. Read a list of complex numbers (in z = a + bi form) from the console.
    2. Display the entire list of numbers on the console.
    3. Display on the console the longest sequence that observes a given property. Each student will receive 2 of the
     properties from the list provided below.
    4. Exit the application.

Sequence Properties:
1 -> 3.Numbers having the same modulus.
2 -> 7.The difference between the modulus of consecutive numbers is a prime number.

'''

# UI section
# (write all functions that have input or print statements here). 
# Ideally, this section should not contain any calculations relevant to program functionalities


def read_complex(list):
    r = input("Real part: ")
    im = input("Imaginary part: ")
    complex = set_complex(r, im)
    add_to_list(list, complex)


def print_list_of_complex(list):
    print("\nThe list is:")
    for i in range(len(list)):
        print(to_str(list[i]), end=';\t')


def print_sequence(list, prop):
    print("\nThe sequence with property " + str(prop) + " is:")
    s = find_seq(list, prop)
    start = s[0]
    end = s[1]
    for i in range(start, end + 1):
        print(to_str(list[i]))


def print_menu():
    print("\nMenu:")
    print("   g -> get a list ")
    print("   + -> add a complex number to list")
    print("   1 -> see the longest sequence with numbers having the same modulus")
    print("   2 -> see the longest sequence where the difference between the modulus of consecutive numbers is a prime number")
    print("   x -> exit")


def start():
    list = []
    print("\nList empty")
    while True:
        print_menu()
        option = input("Option: ")
        if option == 'x':
            return
        elif option == 'g':
            get_a_list(list)
            print_list_of_complex(list)
        elif option == '+':
            read_complex(list)
            print_list_of_complex(list)
        elif option == '1' or option == '2':
            if len(list)==0:
                print ("List is still empty.")
            else:
                print_list_of_complex(list)
                print_sequence(list, int(option))
        else:
            print("invalid input")


# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

from math import sqrt


def set_complex(real, imaginary):
    real = int(real)
    imaginary = int(imaginary)
    return [real, imaginary]


def get_a_list(list):
    complex = set_complex(2, 3)
    add_to_list(list, complex)
    complex = set_complex(3, -2)
    add_to_list(list, complex)
    complex = set_complex(1, 1)
    add_to_list(list, complex)
    complex = set_complex(4, 1)
    add_to_list(list, complex)
    complex = set_complex(-4, 1)
    add_to_list(list, complex)
    complex = set_complex(-1, -4)
    add_to_list(list, complex)
    complex = set_complex(-1, 4)
    add_to_list(list, complex)
    complex = set_complex(3, 4)
    add_to_list(list, complex)
    complex = set_complex(4, -3)
    add_to_list(list, complex)
    complex = set_complex(0, -3)
    add_to_list(list, complex)


def get_real(c):
    return c[0]


def get_imaginary(c):
    return c[1]


def to_str(complex):
    if get_real(complex) != 0:
        if get_imaginary(complex) > 1:
            return str(get_real(complex)) + "+" + str(get_imaginary(complex)) + "i"
        elif get_imaginary(complex) == 1:
            return str(get_real(complex)) + "+" + "i"
        elif get_imaginary(complex) < 0:
            return str(get_real(complex)) + str(get_imaginary(complex)) + "i"
        else:
            return str(get_real(complex))
    else:
        if get_imaginary(complex) != 0:
            return str(get_imaginary(complex)) + "i"
        else:
            return str(get_real(complex))


def add_to_list(list, new):
    list.append(new)


def modulus(c):
    """
    The function calculates the modulus of a complex number.
    :param c: complex number (a+bi) as [a,b]
    :return: the modulus ( sqrt(a*a+b*b) )
    """
    R = get_real(c)
    Im = get_imaginary(c)
    return sqrt(R * R + Im * Im)


def same_modulus(c1, c2):
    """
    verifies the equality between the modulus of 2 complex number
    :param c1: the 1st complex number (a+bi) as [a,b]
    :param c2: the 2nd complex number(a+bi) as [a,b]
    :return: True/false
    """
    return modulus(c1) == modulus(c2)


def is_prime(x):
    """
    This function checks if a given number x is a prime number.
    :param x: tested number (x>1)
    :return: True if x is a prime number, False if x is not a prime number
    """
    if x == 2:
        return True
    if x <= 1 or x % 2 == 0:
        return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def diff_between_mod(c1, c2):
    """
    This function verifies if the difference between the modulus of 2 complex numbers is a prime number.
    :param c1: 1st complex number (a+bi) as [a,b]
    :param c2: 2nd complex number (a+bi) as [a,b]
    :return: True/false
    """
    mod1 = modulus(c1)
    mod2 = modulus(c2)
    dif = mod1 - mod2
    if dif < 0:
        dif = -dif
    return is_prime(dif)


def check_prop(c1, c2, pr):
    """
    calls the function which verifies the required property for the complex numbers and returns the result of verification
    :param c1:1st complex number (a+bi) as [a,b]
    :param c2:2nd complex number (a+bi) as [a,b]
    :param pr: index of required property (1 or 2)
    :return: True/false
    """
    if pr == 1:
        return same_modulus(c1, c2)
    else:
        return diff_between_mod(c1, c2)


def find_seq(list, prop):
    """
    The function finds the beginning and the end of the sequence that observes a required property.
    :param list: list of complex numbers
    :param prop: index of required property (1 or 2)
    :return: the position of first and last value that define the longest sequence
    """
    i = j = 0
    start = end = 0
    lmax = 0
    while i < len(list) - 1:
        j = i + 1
        while j <= len(list) - 1 and check_prop(list[j],list[j-1],prop) is True:
            j = j + 1
        j = j - 1
        if j - i + 1 >= lmax:
            lmax = j - i + 1
            start = i
            end = j
        i = j + 1
    return [start, end]


start()


