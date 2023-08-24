def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
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

array = [2,-5523, 342, 43,53, 2, 34]
print(merge_sort(array))