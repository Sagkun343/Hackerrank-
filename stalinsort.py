def stalinsort(arr):
    if len(arr)<=1:
        return arr
    sorted = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i]>=arr[i-1]:
            sorted.append(arr[i])
    return sorted

print(stalinsort([10,20,15,25,5]))
