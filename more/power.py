""" Power """


# rapid exponentiation
def power(a, k):
    if k < 0:
        return float(1 // k)
    result = 1
    while k:
        # if k is odd
        if k % 2 == 1:
            # mul result on a
            result *= a
        # mul a on yourself for next loop
        a *= a
        k //= 2
    return result


print(power(6, -1))
print(power(2, 0))
print(power(100, 10))
print(power(9, 9))
print(power(9, 2))

