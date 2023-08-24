def miniMaxSum(arr):

    # Write your code here
    min_sum = 0
    max_sum = 0
    for i in range(len(arr)-1):
        min_sum += arr[i]
    for i in arr in range(1,len(arr)):
        max_sum += arr[i]
    print(min_sum, end= " ")
    print(max_sum)

list = [2,3,4,5,6]
array2 = miniMaxSum(list)