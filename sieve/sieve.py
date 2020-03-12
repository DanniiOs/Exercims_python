def primes(limit):
    numbers = [True, True] + [True] * (limit-1)
    last_number = 2
    i = last_number
    while last_number ** 2 <= limit:
        i += last_number
        while i <= limit:
            numbers[i] = False
            i += last_number
        j = last_number + 1
        while j < limit:
            if numbers[j]:
                last_number = j
                break
            j += 1
        i = last_number
    return [i + 2 for i, not_crossed in enumerate(numbers[2:]) if not_crossed]
