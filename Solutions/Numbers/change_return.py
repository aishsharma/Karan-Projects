"""
Author: Aishwarya Sharma
Question: Change Return Program - The user enters a cost and then the amount of money given. The program will figure out
            the change and the number of quarters, dimes, nickels, pennies needed for the change.
"""

from decimal import Decimal, getcontext

getcontext().prec = 2


def get_change(cost: Decimal, amount: Decimal)->Decimal:
    return Decimal(cost - amount)


def app():
    cost = Decimal(input("Enter cost: "))
    amount = Decimal(input("Enter amount: "))

    change = get_change(cost, amount)

    print("Your change: ", change)


if __name__ == '__main__':
    app()
