#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Computes the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): The number for which the factorial is calculated.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
