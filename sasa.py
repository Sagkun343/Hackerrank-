def recursion(n):
    if n!= 1 or 0:
        return recursion(n//2)+str(n%2)
    else:
        return str(f"{n}")

def theGreatXor(x):
    num = 0
    l2 = recursion(x)
    for i in range(1,len(l2)):
        if l2[i] == "0":
            num += pow(2,(len(l2)-(i+1)))
    return num

print(theGreatXor(10))