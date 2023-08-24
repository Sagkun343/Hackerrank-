def anagram(s):
    # Write your code here
    if len(s) % 2 == 1:
        return -1
    diff = int(len(s) / 2)
    left = s[:diff]
    right = s[diff:]
    left_index = int(0)
    right_index = int(0)
    while left_index < len(left):
        while right_index < len(right):
            if left[left_index] == right[right_index]:
                diff -= 1
                left_index = left[:left_index] + left[left_index+1:]
            else:
                right_index += 1
        left_index +=1
    return(diff)

st = "xxyxyy"
print(anagram(st))