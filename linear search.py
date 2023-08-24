def linear(array, number):
    for i in range(0, len(array)):
        if number == array[i]:
            return i
    return -1

print(linear([2, 3, 45, 123, 432, 452, 4], 123))
