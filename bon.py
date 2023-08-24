def bonAppetit(bill, k, b):
    sum = 0
    for i in range(len(bill)):
        sum += bill[i]
    sum -= bill[k]
    sum /= 2
    if b == sum:
        print("Bon Appetit")
    else:
        print(int(b - sum))