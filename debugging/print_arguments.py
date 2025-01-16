#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("Usage: ./script.py <arguments>")
else:
    for arg in sys.argv[1:]:  # Start from the second element (skip script name)
        print(arg)