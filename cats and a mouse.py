def difference(a, b):
    if a >= b:
        return (a - b)
    else:
        return (b - a)


def catAndMouse(x, y, z):
    if difference(x, z) < difference(y, z):
        return "Cat A"
    elif difference(x, z) > difference(y, z):
        return "Cat B"
    else:
        return "Mouse C"