def balancedSums(arr):
    left = sum(arr[:0])
    right = sum(arr[1:])
    if left == right:
        return "YES"
    for i in range(0, len(arr)-1):
        left += arr[i]
        right -= arr[i+1]
        if left == right:
            return "YES"
    return "NO"
