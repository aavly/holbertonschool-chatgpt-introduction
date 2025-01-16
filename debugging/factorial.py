#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    try:
        # Ensure an argument is provided
        if len(sys.argv) < 2:
            print("Usage: ./script.py <number>")
            sys.exit(1)

        # Parse the input and calculate the factorial
        n = int(sys.argv[1])
        if n < 0:
            print("Factorial is not defined for negative numbers.")
            sys.exit(1)

        f = factorial(n)
        print(f)

    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)
