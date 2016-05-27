"""
Author: Aishwarya Sharma
Question: Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for
          the next one.
"""

from typing import List

SIZE = 5


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


# Generate next SIZE primes, starting from n
def generate_primes(n: int)->List:
    primes = []
    i = n + 1

    while len(primes) <= SIZE:
        if is_prime(i):
            primes.append(i)
        i += 1

    return primes


def app():
    choice = "y"
    i = 0
    last_prime = 0
    primes = []

    print("Enter \'y\' to keep seeing the primes and any other key to exit.")

    while choice is "y":
        if i == SIZE or primes == []:
            print("Generating primes")
            primes = generate_primes(last_prime)
            i = 0
            last_prime = primes[SIZE - 1]

        print("Next Prime: ", primes[i])

        i += 1

        choice = str(input("Do you want to see the next prime?"))


if __name__ == '__main__':
    app()