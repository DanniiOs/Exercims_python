def classify(number):
    if number <= 0:
        raise ValueError('Number must be an integer greater than zero.')

    classit = sum([x for x in range(1, number) if number % x == 0])
    if classit == number:
        return 'perfect'
    elif classit < number:
        return 'deficient'
    else:
        return 'abundant'
