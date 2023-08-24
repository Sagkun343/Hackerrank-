import math
from math import *

def permutation(n,r):
    if n<r:
        return None
    if n==r or r==0:
        return 1
    BIGGER_DENOMINATOR = max(r, n-r)
    permutation_value = 1
    while n>BIGGER_DENOMINATOR:
        permutation_value *= n
        n -= 1
    return permutation_value

print(permutation(20, 4))

def combination(n,r):
    val = permutation(n,r)
    x = min(r, n-r)
    x = factorial(x)
    return val/x

print(combination(522+575-1, 522))
