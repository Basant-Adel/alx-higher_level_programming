#!/usr/bin/python3
for number in range(0, 9):
    num = number + 1
    while num <= 9:
        print("{:d}{:d}".format(number, num), end='')
        print(end='\n' if number == 8 else ", ")
        num += 1
