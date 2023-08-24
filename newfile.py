list3 = []
l1 = [5, 5, 9, 9, 1, 2, 5]
l2 = [9, 9, 7, 8]
temp = ""
i = 0
current = 0
carry = 0
if len(l1) < len(l2):
    size = len(l2)
else:
    size = len(l1)
while i < size:
    temp = str(l1[i] + l2[i] + carry)
    if int(temp)>9:
        current = int(temp[1])
        carry = int(temp[0])
    else:
        current = int(temp[0])

    list3.append(current)
    if i == size-1 and carry != 0:
        list3.append(carry)
    i += 1

print(list3)
