arr =[]
my_dict = {2 :('a', 'b', 'c'), 3:('d', 'e', 'f'), 4:('g', 'h', 'i'), 5:('j','k','l'),6:('m','n','o'),7:('p','q','r','s'),8:('s','t','u'),9:('w','x','y','z')}
print(my_dict)

print(arr)
input = "234"
def recursive(n):
    if n==1:
        return n
    else:
        return n*recursive(n-1)

print(recursive(2))
