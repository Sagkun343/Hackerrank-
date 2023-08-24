import math


list = []
def thereatXor(x):
    if x ==1:
        return list.append(0)
    if x ==0:
        return None
    y = math.log2(x)
    h = round(pow(2, y)- pow(2, int(y)))
    list.append(int(y)+1)
    return thereatXor(h)
def theGreatXor(arr):
    n = arr[0]
    num = pow(2, (n-len(arr)))-1
    return num
thereatXor(232)
print(theGreatXor(list))
print(list)