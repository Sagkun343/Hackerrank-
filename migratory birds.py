def migratoryBirds(arr):
    my_dict = dict()
    max = 0
    val = 0
    for i in range(len(arr)):
        if arr[i] not in my_dict:
            my_dict[arr[i]] = 1
        else:
            my_dict[arr[i]] += 1
    print(my_dict)
    for key in my_dict:
        if my_dict[key]>val:
            max = key
            val = my_dict[key]
            print(f"val = {val}")
    return max

print(migratoryBirds([1 ,4 ,4 ,4 , 5, 3]))