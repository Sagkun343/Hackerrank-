array = [21, 12, 42, 54, 566, 34, 82832, 28.5,223]
def merge_sort(list):
    midpoint = len(list) // 2
    if len(list) <= 1:
        return list
    left_half = list[:midpoint]
    right_half = list[midpoint:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

def merge(left, right):
    i = 0
    j = 0
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

sorted_array = merge_sort(array)
print(sorted_array)
