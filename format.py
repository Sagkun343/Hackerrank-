def genepool(str):
    a = g = c = t = 0
    for i in range(len(str)):
        if str[i] == 'A':
            a += 1
        elif str[i] == 'G':
            g += 1
        elif str[i] == 'C':
            c += 1
        else:
            t += 1
    optimal = len(str)/4
    if a == g == c == t:
        return 0
    
print(genepool("AAGGCCTT"))