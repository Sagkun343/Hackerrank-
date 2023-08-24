arr = [120, 42, 421, 53, 31]
key = 0
length = len(arr)
print(length)
var = 0
for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        arr[j] = key
        j -= 1

print(arr)
