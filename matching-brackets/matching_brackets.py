def is_paired(input_string):
    cadena = [x for x in input_string if x in "{}[]()"]
    if len(cadena) % 2 != 0:
        return False
    else:
        return True
        i = 0
        while i <= len(cadena) and True:
            if cadena[i] in "{[(":
                i += 1
            else:
                if cadena[i - 1] + cadena[i] in "{}" or \
                        cadena[i - 1] + cadena[i] in "[]" or \
                        cadena[i - 1] + cadena[i] in "()":
                    cadena = cadena[:i - 1] + cadena[i + 1:]
                    i -= 1
                else:
                    return False

print(is_paired("}{"))
