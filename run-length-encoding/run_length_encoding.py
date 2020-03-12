from re import sub


def encode(string):
    return sub(
        r"(.)\1*",
        lambda m: str(len(m.group())) + m.group()[0]
        if len(m.group()) > 1
        else m.group()[0],
        string,
    )


def decode(string):
    return sub(
        r"(\d*\D)\1*",
        lambda m: m.group()[-1] * int(m.group()[:-1])
        if len(m.group()) > 1
        else m.group(),
        string,
    )
