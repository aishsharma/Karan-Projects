"""
Author: Aishwarya Sharma
Question: Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number
          or to the Nth number.
"""

from typing import List
from math import sqrt


# Generates fibonacci sequence up to n
# OR if n is not a fibonacci number then generate n fibonacci numbers
def generate_fibonacci(n: int)->List:

    # Testing if n is fibonacci
    x = (5*(n**2) + 4)
    y = (5 * (n ** 2) - 4)
    if is_square(x) or is_square(y):
        flag = True
    else:
        flag = False

    first = 0
    second = 1
    third = -1
    fibo_sequence = []

    if n < 3:
        print("Input should be an at least 3")
        return fibo_sequence

    fibo_sequence.append(first)
    fibo_sequence.append(second)

    if flag:
        while third != n:
            third = first + second
            fibo_sequence.append(third)
            first = second
            second = third

    else:
        while len(fibo_sequence) < n:
            third = first + second
            fibo_sequence.append(third)
            first = second
            second = third

    return fibo_sequence


# Tests if n is a perfect square and then returns True/False
def is_square(n: int)->bool:
    if round(sqrt(n))**2 == n:
        return True
    else:
        return False


def main():

    flag = True

    while flag:
        try:
            n = int(input("Enter a number: "))

            fibo = generate_fibonacci(n)

            if not fibo:
                print("No sequence generated. You may have had an error")
            else:
                print("Your sequence is: ")
                print(fibo)
                flag = False
        except ValueError:
            print("Input should be an integer. Try again")


if __name__ == "__main__":
    main()
