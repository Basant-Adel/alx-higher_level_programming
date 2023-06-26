#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = []

    for a in range(list_length):

        b = 0

        try:
            b = my_list_1[a] / my_list_2[a]

        except TypeError:
            print("wrong type")

        except ZeroDivisionError:
            print("division by 0")

        except IndexError:
            print("out of range")

        finally:
            new_list.append(b)

    return new_list
