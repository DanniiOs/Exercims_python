from string import ascii_uppercase


def rows(letter):
    n = ascii_uppercase.index(letter)
    return [
        "".join(ascii_uppercase[abs(i)] if abs(j) + abs(i) == n else " "
                for i in range(-n, n + 1)) for j in range(-n, n + 1)
    ]
