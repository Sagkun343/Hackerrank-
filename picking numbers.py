def pickingNumbers(a):
    substring_counter = 0
    substring_dict = {}
    for i in range(len(a)):
        if a[i] not in substring_dict:
            substring_dict[a[i]] = 1
        else:
            substring_dict[a[i]] += 1
    for key in substring_dict:
        trick = key +1
        if trick in substring_dict:
            if substring_dict[key]+ substring_dict[trick]> substring_counter:
                substring_counter = substring_dict[key] + substring_dict[trick]
        else:
            if substring_dict[key]>substring_counter:
                substring_counter = substring_dict[key]

    return substring_counter

print(pickingNumbers([4,6,5,3,3,1]))