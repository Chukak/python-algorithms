""" Selection sorting """

array = [234, 345, 4, 32, 45455, 56, 76, 345, 46, 8678676, 567, 43, 2, 5, 8, 105, 4, 17]


def selection_sorting_stable(array):
    for i in range(len(array)):
        minimum = i
        for m in range(i+1, len(array)):
            minimum = m if array[m] < array[minimum] else minimum
        if i != minimum:
            value = array[minimum]
            for j in range(minimum, i-1, -1):
                array[j] = array[j-1]
            array[i] = value


def selection_sorting_2(array):
    for i in range(len(array)):
        x, j = i, i + 1
        while j <= len(array) -1:
            if array[x] > array[j]:
                x = j
            j += 1
        array[x], array[i] = array[i], array[x]


selection_sorting_stable(array)
print(array)
selection_sorting_2(array)
print(array)

