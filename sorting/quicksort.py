""" Quicksort sorting """
import random

array = [234, 345, 4, 32, 45455, 56, 76, 345, 46, 8678676, 567, 43, 2, 5, 8, 105, 4, 17]


def quicksort(array):
    if not array:
        return []
    element = random.choice(array)
    less = list(filter(lambda x: x < element, array))
    equally = list(filter(lambda x: x == element, array))
    more = list(filter(lambda x: x > element, array))
    return quicksort(less) + equally + quicksort(more)


def quicksort_2(array):
    if array:
        element = random.choice(array)
        return quicksort_2([x for x in array if x < element]) + \
            [x for x in array if x == element] + quicksort_2([x for x in array if x > element])
    else:
        return []





print(quicksort(array))
#print(quicksort_2(array))


