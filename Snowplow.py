from math import trunc

import numpy


# Function to calculate the average waiting time for each house and return the average waiting time

def waiting_time(main_list):
    finale = 0
    for h in main_list:
        i = 0
        snowplow = 0
        wtime = abs(main_list[0])
        while main_list[i] != h:
            i += 1
            if main_list[i] * snowplow > 0:
                wtime += abs(abs(main_list[i]) - abs(snowplow))
            else:
                wtime += abs(abs(main_list[i]) + abs(snowplow))
            snowplow = h
        finale += wtime
    return finale / len(main_list)


# Function which return the closest house

def closer(main_list, h):
    if len(main_list) == 1:
        return main_list[0]
    i = abs(main_list.max()) + abs(main_list.min())
    res = main_list.max()
    for k in main_list:
        if h * k > 0:
            x = abs(abs(h) - abs(k))
        else:
            x = abs(abs(h) + abs(k))
        if x < i:
            i = x
            res = k
    return res

# Function which sort to put each house to the closest one to optimize the travel of snowplow, try with each house at
# first and return the ist with the less average waiting time


def mySort2(main_list):
    finalist = main_list
    for h in main_list:
        if abs(h) > abs(finalist[1]):
            continue
        ret = main_list
        tmp_list = []
        nxt = h
        i = 0
        while i < len(main_list):
            tmp = closer(ret, nxt)
            ret = numpy.delete(ret, numpy.where(ret == tmp))
            tmp_list.append(tmp)
            i += 1
            nxt = tmp
        if waiting_time(finalist) > waiting_time(tmp_list):
            finalist = tmp_list
    return finalist

# Main function


def parcours(res_list):
    print(res_list)
    print("AVG1:")
    print(waiting_time(res_list))
    list3 = mySort2(res_list)
    print("AVG AFTER SORT:")
    print(waiting_time(list3))
    return list3


print(parcours(numpy.random.normal(0, 100, 100)))
