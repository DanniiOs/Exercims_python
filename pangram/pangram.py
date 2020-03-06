def is_pangram(sentence) -> bool:
    import string
    alphabet = set(string.ascii_lowercase) - set(sentence.lower())
    return not alphabet
