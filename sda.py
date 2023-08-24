def plusMinus(arr):
    # Write your code here
    positive = 0 
    negative = 0
    zero = 0
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            zero += 1
            i += 1
        elif arr[i]>0:
            positive += 1
            i += 1
        else:
            negative += 1
            i += 1
    positive_ratio = float(positive / len(arr))
    negative_ratio = float(negative / len(arr))
    zero_ratio = float(1 - positive_ratio - negative_ratio)
    return f"{positive_ratio:.6f}\n{negative_ratio:.6f}\n{positive_ratio:.6f}"


array = [2,-3,0,-5,-6,2,4,56,-23,0]
print(plusMinus(array))