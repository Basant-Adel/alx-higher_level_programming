#!/usr/bin/python3
def fizzbuzz():
    for ba in range(1, 101):
        if((ba % 3 == 0) and (ba % 5 == 0)):
            print('FizzBuzz', end=' ')
        elif(ba % 3 == 0):
            print('Fizz', end=' ')
        elif(ba % 5 == 0):
            print('Buzz', end=' ')
        else:
            print('{:d} '.format(ba), end='')
