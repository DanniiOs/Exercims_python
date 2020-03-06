import re


def abbreviate(words):
    words = re.sub(r"[^a-zA-Z' ]", " ", words.upper())
    acronym = ''.join(word[0] for word in words.split())
    return acronym
