#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("Usage: ./script.py <arguments>")
else:
    for i in range(len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")
