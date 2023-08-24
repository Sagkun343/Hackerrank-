def rotated_array(arr):
    lower_limit = 0
    print(lower_limit)
    upper_limit = (len(arr))-1
    print(upper_limit)
    midpoint =0
    while lower_limit!=upper_limit:
        midpoint = ((lower_limit + upper_limit)//2)
        print(f"midpoint is {arr[midpoint]}")
        if arr[lower_limit]>arr[midpoint]:
            upper_limit = midpoint
            print(f"upper limit is now {upper_limit}")
        elif arr[lower_limit]<arr[midpoint]:
            lower_limit = midpoint
            print(f"lower limit is now {lower_limit}")
        else:
            return midpoint
    return upper_limit

print(rotated_array([5,5,6,6,6,7,7,12,12,12,3,4]))

