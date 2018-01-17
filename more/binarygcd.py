""" Binary gcd algorithm """


def binary_gcd(a, b):
    # check a,b is 0 or 1 or a == b
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a == 1 or b == 1:
        return 1
    elif a == b:
        return a
    # recursive
    else:
        if a % 2 == 1 and b % 2 == 1:
            return binary_gcd(a, (b-a)//2) if b > a else binary_gcd((a-b)//2, b)
        elif a % 2 == 0 and b % 2 == 1:
            return binary_gcd(a//2, b)
        elif a % 2 == 1 and b % 2 == 0:
            return binary_gcd(a, b//2)
        else:
            return 2 * binary_gcd(a // 2, b // 2)


def binary_gcd_2(a, b):
    # get abs a and b >=0
    a, b = abs(a), abs(b)
    if a < b:
        a, b = b, a  # a >= b >= 0
    if b == 0:
        return a
    # a >= b >= 0
    # k = num, for formula 2 * CGD(a//2, b//2), where 2 = num
    k = 1
    # a and b is even
    print(a,b)
    while a % 2 == 0 and b % 2 == 0:
        k = k * 2
        a, b = a // 2, b // 2
    print(a, b, k)
    t = b * -1 if a % 2 else a
    print(t)
    while t:
        while t % 2 == 0:
            t //= 2
        print(t)
        if t > 0:
            a = t
        else:
            b = t * -1
        t = a - b
    return a * k


print(binary_gcd(680, 612))
print(binary_gcd_2(680, 612))
