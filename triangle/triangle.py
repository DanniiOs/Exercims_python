def equilateral(sides):
    if a == b and a == c:
        return True
    else:
        return False


def isosceles(a, b, c):
    if (a != b and a == c) or (a == b and a != c):
        return True
    else:
        return False


def scalene(a, b, c):
    if a != b and a != c:
        return True
    else:
        return False
