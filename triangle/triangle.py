def equilateral(sides):
    return len(set(sides)) == 1 and isTriangle(sides)


def isosceles(sides):
    return len(set(sides)) < 3 and isTriangle(sides)


def scalene(sides):
    return len(set(sides)) > 2 and isTriangle(sides)


def isTriangle(sides):
    return (sides[0] < (sides[1] + sides[2]) and sides[1] < (sides[0]+sides[2])
            and sides[2] < (sides[0]+sides[1]))
