#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    list1 = sum(map(lambda ml: ml[0] * ml[1], my_list))
    list2 = sum(map(lambda ml: ml[1], my_list))
    return list1 / list2
