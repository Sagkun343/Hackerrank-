def powersum(x:int, n:int):
    my_set = {1}
    for i in range(2,x+1):
        if pow(i,n)<x:
            my_set.add(pow(i,n))
        else:
            break
    for
    return my_set

print(powersum(13,2))
