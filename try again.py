def pairs(k, arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i]-arr[j]) == k:
                count += 1
    return count

print(pairs(2,[1,5,3,4,2]))