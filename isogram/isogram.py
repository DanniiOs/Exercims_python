def is_isogram(string):
    string = string.upper().replace('-', '').replace(' ', '')
    for i, let in enumerate(string, 1):
        if let in string[i:]:
            return False
    return True
