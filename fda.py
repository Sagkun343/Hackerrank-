ar = [[24,3,1,5,6],[2,3,4,3,6],[2,3,4,5,6],[2,3,4,5,6],[2,3,4,5,6]]
def diagonalDifference(arr):
    # Write your code here
    i= 0
    sum1 = 0
    sum2 = 0
    difference = 0
    while i<len(arr):
        sum1 += arr[i][i]
        #print(arr[i][i])
        sum2 += arr[len(arr)-1-i][i]
        i += 1
    difference = diff(sum1, sum2)
    return difference
def diff(num1, num2):
    d = 0
    if num1>num2:
        d = num1 - num2
        return d
    elif num2>num1:
        d = num2 - num1
        return d
    else:
        return 0

print(float(diagonalDifference(ar)))
