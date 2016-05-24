"""
Author: Aishwarya Sharma
"""

from math import e
from decimal import Decimal, getcontext


getcontext().prec = 100
E = Decimal(e)


# n = Number of digits. Must be between 1 and 51
def find_e_to_digit(n: int)->str:
    if n < 1 or n > 50:
        return "Input should be between 1 and 51"
    else:
        E_str = str(E)
        length_of_E = len(E_str) - 2
        result = E_str[:-(length_of_E - n)]

    return result

if __name__ == "__main__":
    x = find_e_to_digit(50)
    print(x)
    print(len(x) - 2)
