def staircase(n):
    # Write your code here
    i = 1
    while i<=n:
        for j in range(0,n-i):
            print(' ', end='')
        for k in range(0,i):
            print('#', end='')
            if k == i-1:
                print('')
        i += 1


print(staircase(10))