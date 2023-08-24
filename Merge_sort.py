
array = [2,-5523, 342, 43,53, 54, 54, 2, 34]
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)
def merge(left, right):
    i= 0
    j= 0
    l = []
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    l.extend(left[i:])
    l.extend(right[j:])
    return l

print(merge_sort(array))
array.sort()
box = -1
sorted = []
for num in range(len(array)):
    if array[num] != box:
        box = array[num]
        sorted.append(array[num])
print(sorted)