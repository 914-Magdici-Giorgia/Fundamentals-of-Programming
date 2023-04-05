# Solve the problem from the third set here
"""
Set 3, ex 15
Generate the largest perfect number smaller than a given natural number n. If such a number does not exist, a message
should be displayed. A number is perfect if it is equal to the sum of its divisors, except itself. (e.g. 6 is a perfect
number, as 6=1+2+3).
"""
def verif_perfect_number(x):
    """
    This function verifies if a given natural number x is perfect (equal to the sum of its divisors, except itself).
    :param x: natural number (x>0)
    :return: True if the property is checked, False otherwise.
    """
    sum=0;
    for divisor in range (1, x//2 +1):
        if x % divisor==0:
            sum=sum+divisor
    return x==sum


def generate(n):
    """
    This function finds the largest perfect number smaller than a given natural number n.A number is perfect if it is
    equal to the sum of its divisors, except itself.
    :param n: natural number (n>0)
    :return: True if a perfect number smaller than n exists and the number we were looking for, False otherwise
    """
    found=False
    n=n-1
    while n>0 and found is False :
        found=verif_perfect_number(n)
        if found is False:
            n=n-1
    return found,n


if __name__=="__main__":
    n=int(input("n= "))
    exists, result=generate(n)
    if exists  is True:
        print (result)
    else:
        print ("it doesn't exist")



