def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob.endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif str.isupper(hey_bob):
        return("Whoa, chill out!")
    elif hey_bob.endswith("?"):
        return "Sure."
    elif hey_bob == "":
        return ("Fine. Be that way!")
    else:
        return ("Whatever.")
