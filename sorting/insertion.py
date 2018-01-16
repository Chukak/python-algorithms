""" Insertion sort """

array = [234, 345, 4, 32, 45455, 56, 76, 345, 46, 8678676, 567, 43, 2, 5, 8, 105, 4, 17]


def insertion_sort(array):
    for i in range(len(array)):
        x = i
        for j in range(i + 1, len(array)):
            if array[x] > array[j]:
                x = j
        array[x], array[i] = array[i], array[x]


insertion_sort(array)
print(array)