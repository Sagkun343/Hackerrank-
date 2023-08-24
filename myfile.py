def myfactorial(n):
    if n == 1: 
        return [1]
    else: 
        return myfactorial(n-1) + [n * myfactorial(n-1)[n-2]]

print(myfactorial(6))