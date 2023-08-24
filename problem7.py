def fun(n):
    k = 0
    num1 = 0
    num2 = 0
    num3 = 1
    arr = []
    while k <= n - 1:
        arr.append(num3)
        num1 = num2
        num2 = num3
        num3 = num1+num2
        k = k + 1
        continue
    return arr

print(fun(5))