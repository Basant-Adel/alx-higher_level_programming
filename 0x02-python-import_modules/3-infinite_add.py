#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) - 1 == 0:
        print("0")
    else:
        sum = 0
        for b in range(len(argv) - 1):
            add = int(argv[b + 1])
            sum += add
        print("{:d}".format(sum))
"""
if-name=main-> To only run the code inside the if statement,
When the program is run directly by the Python interpreter.
From..import..->when u need 2 use its code many times in your code project.
"""
