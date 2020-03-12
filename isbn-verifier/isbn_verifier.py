def is_valid(isbn):
    digits = isbn[:-1].replace("-", "")
    if len(digits) != 9 or set(digits) - set("0123456789"):
        return False
    if isbn[-1] not in "0123456789X":
        return False
    final = 10 if isbn[-1] == "X" else int(isbn[-1])
    return (sum
            (i * int(digits[10 - i]) for i in range(2, 11)) + final) % 11 == 0
