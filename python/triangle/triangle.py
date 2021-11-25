def equilateral(sides):

    if len(sides) != 3:
        return False

    for measurement in sides:
        if measurement <= 0:
            return False

    comparator = sides[0]
    counter = 1
    num_equal_sides = 1

    while counter < len(sides):
        if comparator == sides[counter]:
            num_equal_sides += 1
        counter += 1

    if num_equal_sides == 3:
        return True

    return False


# ==============================================
# ==============================================


def isosceles(sides):

    if len(sides) != 3:
        return False

    if equilateral(sides) is True:
        return True

    for measurement in sides:
        if measurement <= 0:
            return False

    if ((sides[0] + sides[1]) <= sides[2]) or\
        ((sides[0] + sides[2]) <= sides[1]) or\
            ((sides[1] + sides[2]) <= sides[0]):
        return False

    comparator = sides[0]
    counter = 1
    num_equal_sides = 1

    while counter < len(sides):
        if comparator == sides[counter]:
            num_equal_sides += 1
        counter += 1

    if num_equal_sides >= 2:
        return True

    comparator = sides[1]
    counter = 2
    num_equal_sides = 1

    while counter < len(sides):
        if comparator == sides[counter]:
            num_equal_sides += 1
        counter += 1

    if num_equal_sides >= 2:
        return True

    return False


# ==============================================
# ==============================================


def scalene(sides):

    if len(sides) != 3:
        return False

    if isosceles(sides) is True:
        return False

    if ((sides[0] + sides[1]) <= sides[2]) or\
        ((sides[0] + sides[2]) <= sides[1]) or\
            ((sides[1] + sides[2]) <= sides[0]):
        return False

    for measurement in sides:
        if measurement <= 0:
            return False

    return True
