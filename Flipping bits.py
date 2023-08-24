def binary(n):
    if n == 0 or n == 1:
        return f"{n}"
    else:
        return binary(n // 2) + str(n % 2)
def flippingBits(n):
    key = int(binary(n))
    l = 900000000000000000000000000000000
    num = str(key+l)
    new_num = num[1:]
    num = ""
    for i in range(32):
        if new_num[i] == "0":
            num += "1"
        else:
            num += "0"
    new_num = 0
    for k in range(32):
        if num[k] == "1":
            new_num += pow(2,31-k)
    return new_num


print(flippingBits(9))

