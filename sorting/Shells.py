""" Shells sort """

array = [234, 345, 4, 32, 45455, 56, 76, 345, 46, 8678676, 567, 43, 2, 5, 8, 105, 4, 17]
# array = [1001, 10, 17]


def shells_sort(array):
    num = len(array) // 2
    # step 2
    while num >= 1:
        # get index and value
        for i, value in enumerate(array):
            print(i, value, num)
            j = i
            # equals value
            # Example: you have range (0, j-num), you needs check value array[i] and array[j-num]
            # i = 0, j = 0, num = 9 --> don`t loop
            # i = 17, j = 17, num = 9 --> 1 loop ( 17-9=8 and 17 < 46 )
            # i = 17, j = 17, num = 4 --> 3 loop ( 17-4=13 and 46 < 8678676, 13-4=9 and 46 < 45455, 9-4=5 and 46 < 345,
            #                                      5-4=1 and 46 < 8 )
            while j - num >= 0 and value < array[j - num]:
                # Uncomment this string and string at line 4 and watching order in list
                # print(j, num, value, array[j-num], 'values')
                # print(array)
                array[j] = array[j-num]
                j -= num
            array[j] = value
        num //= 2


shells_sort(array)
print(array)
