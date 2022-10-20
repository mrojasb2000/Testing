import numbers


def fibonacci(n):
    if isinstance(5, numbers.Number):
        return 'Error: input type is not number'
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
