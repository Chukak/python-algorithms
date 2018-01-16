""" Sort by minimum search """

array = [234, 345, 4, 32, 45455, 56, 76, 345, 46, 8678676, 567, 43, 2, 5, 8, 105, 4, 17]


def min_search_sort(array):
    for i in range(len(array)):
        minimum = min(array[i:])
        index = array.index(minimum)
        if minimum < array[i]:
            array[i], array[index] = minimum, array[i]
    return array


def min_search_sort_2(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return array


print(min_search_sort(array))
#print(min_search_sort_2(array))

