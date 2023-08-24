arr = [1, 2, 3, 4, 5, 6, 7]
rev = []
z = len(arr)
for i in range(0, len(arr)):
    rev.append(arr[z-1])
    i += 1
    z -= 1

print(rev)
