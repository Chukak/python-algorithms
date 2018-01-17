""" Factorial """


def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)


def factorial_2(n):
    result = n
    while n > 1:
        result, n = result * (n - 1), n - 1
    return result if result > 0 else 1


print(factorial(10))
print(factorial_2(10))

