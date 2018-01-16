""" Merge sort """

array = [234, 345, 4, 32, 45455, 56, 76, 345, 46, 8678676, 567, 43, 2, 5, 8, 105, 4, 17]


def merge(left, right, result):
    lst = left if left[0] < right[0] else right
    result.append(lst.pop(0))
    return merge(left=left, right=right, result=result) if left and right else result + left + right


def sorting(array):
    if len(array) > 1:
        # recursive call func until 1 element is left in array
        return merge(sorting(array[len(array)//2:]), sorting(array[:len(array)//2]), [])
    else:
        return array


print(sorting(array))




