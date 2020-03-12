def map_char(c):
    return chr(ord('a')+ord('z')-ord(c.lower())) if c.isalpha() else c


def encode(plain_text):
    d = decode(plain_text)
    return ' '.join(d[k:k+5] for k in range(0, len(d), 5))


def decode(ciphered_text):
    return ''.join(map_char(c) for c in ciphered_text if c.isalnum())
