import math
def counterGame(n):
    if n == 1:
        return "Richard"
    k = 0
    while n != 1:
        count = 0
        x = math.log2(n)
        if int(x) == x:
            if x%2 == 0:
                return "Louise"
            else:
                return "Richard"
        else:
            y = math.floor(x)
            k = pow(2, (x-y))
            n = k

counterGame(132)