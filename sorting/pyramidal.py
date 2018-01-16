""" Pyramidal sorting """


array = [234, 345, 4, 32, 45455, 56, 76, 345, 46, 8678676, 567, 43, 2, 5, 8, 105, 4, 17]


def pyramidal_sort(array):
    """ This sorting sort ascending.
    If you want sort descending, replace all < on > at row with #! symbol."""
    def sift_down(parent, length, item):
        child = parent * 2 + 1
        if child < length:
            if child + 1 < length and array[child] < array[child +1]: #!
                child +=1
            if item < array[child]: #!
                array[parent] = array[child]
                return sift_down(child, length, item)
        return parent, item

    for i in range(len(array) // 2 - 1, -1, -1):
        pos, item = sift_down(i, len(array), array[i])
        array[pos] = item

    for j in range(len(array) - 1, 0, -1):
        array[0], array[j] = array[j], array[0]
        pos, item = sift_down(0, j, array[0])
        array[pos] = item


pyramidal_sort(array)
print(array)
