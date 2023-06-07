#!/usr/bin/python3
def uppercase(str):
    for upper_c in str:
        print("{:c}".format(65 + (ord(upper_c) - 97)
                            if ord(upper_c) >= 97 and ord(upper_c) <= 122
                            else ord(upper_c)), end="")
    print("")
