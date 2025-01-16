#!/usr/bin/python3
import sys

def factorial(n):
    """
    Computes the factorial of a given non-negative integer n using recursion.

    The factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n.
    Specifically:
        factorial(n) = n * (n-1) * (n-2) * ... * 1
    For n = 0, factorial(0) is defined as 1.

    Parameters:
    n (int): The non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the input integer n.
    """
    if n == 0:
        # Base case: factorial of 0 is 1
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Main execution starts here
if __name__ == "__main__":
    # Ensure that the user has provided a command-line argument
    if len(sys.argv) < 2:
        print("Usage: ./factorial_recursive.py <number>")
        sys.exit(1)

    try:
        # Convert the command-line argument to an integer
        n = int(sys.argv[1])

        # Ensure the number is non-negative
        if n < 0:
            print("Factorial is not defined for negative numbers.")
            sys.exit(1)

        # Call the factorial function and print the result
        f = factorial(n)
        print(f)

    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Please provide a valid integer.")
        sys.exit(1)
