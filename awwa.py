import math
def counterGame(n):
    if n == 1:
        return "Richard"
    k = 0
    x = math.log2(n)
    if int(x) == x:
        if x%2 == 0:
            return "Louise"
        else:
            return "Richrd"
    else:
        k = round(pow(2,x) - pow(2, int(x)))
        n = k
        print(n)
        return counterGame(n)

print(counterGame(232))
