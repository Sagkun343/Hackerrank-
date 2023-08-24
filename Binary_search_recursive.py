def binary_recursion(target, array):
    midpoint = len(array) // 2
    if len(array) == 0:
        return False
    elif target == array[midpoint]:
        return True
    elif target > array[midpoint]:
        return binary_recursion(target, array[midpoint + 1:])
    else:
        return binary_recursion(target, array[:midpoint])


print(binary_recursion(100, [2, 4, 6, 7, 100]))
