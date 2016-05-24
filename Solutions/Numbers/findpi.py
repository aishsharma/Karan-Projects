from math import pi
from decimal import Decimal, getcontext

__author__ = "Aishwarya Sharma"


my_pi = str(pi)
length_of_pi = len(my_pi)-2


# Returns the number pi up to n digits as a string
def get_pi_to_digit(n: int)->str:

    # Sanity check, n should be greater than 0
    if n < 1:
        result = "Input should be greater than 0"
    elif n <= length_of_pi:
        result = my_pi[:-(length_of_pi - n)]
    else:
        result = str(bbp(n))

    return result


# Using BBP formula to calculate nth digit of Pi.
# Reference: https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
def bbp(n: int)->int:
    getcontext().prec = n + 1
    result = 0
    for k in range(n):
        result += (1/(Decimal(16)**k)) * ((Decimal(4)/(8*k + 1)) - (Decimal(2)/(8*k + 4)) - (Decimal(1)/(8*k + 5)) -
                                          (Decimal(1)/(8*k + 6)))

    return result


if __name__ == "__main__":
    x = get_pi_to_digit(4000)
    print(x)
    print(len(x) - 2)
