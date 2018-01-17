""" gcd algorithm """


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_2(a, b):
    return gcd(b, a % b) if b else a


print(gcd(680, 612))
print(gcd_2(680, 612))