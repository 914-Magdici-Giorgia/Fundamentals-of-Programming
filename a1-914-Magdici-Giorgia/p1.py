# Solve the problem from the first set here
#set1, prob 3
"""
For a given natural number n find the minimal natural number m formed with the same digits. (e.g. n=3658, m=3568).
"""
def count_appearances (n,d):
    """
    This function counts how many times the digit d appears in the natural number n.
    :param n: natural number (n>=0)
    :param d: a digit (0<= d <=9)
    :return: how many times d appears in n
    """
    count = 0
    while n != 0:
        if n % 10 == d:
            count+=1
        n//=10
    return count

def min_digit(n):
    min=9
    while n>0:
        if n%10<min and n%10!=0:
            min=n%10
        n=n//10
    return min

def minimal_number_with_same_digits(n):
    """
    This function finds the minimal natural number m formed with the same digits as the given natural number n.
    :param n: natural number (n>=0)
    :return: the minimal natural number m formed with the same digits
    """
    min=min_digit(n)
    m=min
    for digit in range(10):
        k=count_appearances (n,digit)
        if digit ==min:
            k=k-1
        for i in range(1, k+1):
            m=m*10+digit
    return m




if __name__=="__main__":
    n = int(input("n= "))
    print(minimal_number_with_same_digits(n))




