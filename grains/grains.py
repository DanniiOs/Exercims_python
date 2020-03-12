def square(number):
    if number < 1 or number > 64:
        raise ValueError("n < 1")
    return 2 ** (number-1)


def total():
    return sum([2 ** i for i in range(0, 64)])
