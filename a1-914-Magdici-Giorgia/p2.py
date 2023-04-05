# Solve the problem from the second set here
# set 2, problem 7
"""
Determine the twin prime numbers p1 and p2 immediately larger than the given non-null natural number n. Two prime
numbers p and q are called twin if q - p = 2.
"""
from math import sqrt


def is_prime(x):
    """
    This function checks if a given natural number x is a prime number.
    :param x: natural number (x>1)
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


def twin_prime_nrs_immediately_larger(n):
    """
    The function is looking for a pair of twin prime numbers immediately larger than the given non-null natural number n
    :param n: a non-null natural number (n>0)
    :return: the twin prime numbers twin_1 and twin_2 immediately larger than n.
    """
    twin_1 = twin_2 = 0
    p = int(n + 1)  # the immediately larger number
    while twin_2 == 0:
        if is_prime(p) is True:
            q = p + 2  # a number that could be the twin of p
            if is_prime(q) is True:
                twin_1 = p
                twin_2 = q
        p = p + 1  # the next tested number
    return twin_1, twin_2


if __name__ == "__main__":
    n = int(input("n= "))
    print(twin_prime_nrs_immediately_larger(n))
