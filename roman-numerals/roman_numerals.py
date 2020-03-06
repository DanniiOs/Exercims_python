def roman(number):
    if not 0 < number < 3001:
        raise ValueError("Argument must be between 1 and 3000")
    ints = (1000, 900,  500, 400, 100,  90,
            50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL',
            'X', 'IX', 'V', 'IV', 'I')
    result = []
    for i in range(len(ints)):
        count = int(number / ints[i])
        result.append(nums[i] * count)
        number -= ints[i] * count
    return ''.join(result)
