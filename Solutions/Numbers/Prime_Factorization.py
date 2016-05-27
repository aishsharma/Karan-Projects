"""
Author: Aishwarya Sharma

Question: Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display
            them.
"""

from math import sqrt
from typing import List


# Tests if a number is prime or not. Uses simple formula for test.
def is_prime(n: int)->bool:
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False

    i = 5
    while i**2 <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i += 6

    return True


def get_prime_factors(n: int)->List:

    if n < 2:
        print("Input should be at least 2.")
        return []
    elif is_prime(n):
        print("Input is a prime number")
        return []

    prime_factors = []

    for i in range(2, round(sqrt(n)) + 1):
        if n % i == 0 and is_prime(i):
            prime_factors.append(i)

    return prime_factors


def app():
    try:
        n = int(input("Enter a number and I will give you its prime factors: "))
    except ValueError:
        print("Input must be a number > 1")

    prime_factors = get_prime_factors(n)

    print("The prime factors of {0} are: ".format(n))
    print(prime_factors)


if __name__ == '__main__':
    app()
