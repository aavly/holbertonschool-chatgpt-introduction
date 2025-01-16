#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function to calculate the factorial of a number recursively.

    Parameters:
        n (int): The non-negative integer for which the factorial is to be computed.

    Returns:
        int: The factorial of the input number `n`. 
             If n is 0, the factorial is defined as 1.

    Example:
        factorial(4) will return 24 since 4! = 4 * 3 * 2 * 1 = 24.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the number from command-line arguments
f = factorial(int(sys.argv[1]))

# Print the result
print(f)