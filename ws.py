Dict = {0: 21, 1: 50, 2: 70, 3: 100}
sum = 0
for a in range(len(Dict)):
    sum += Dict[a]
    if a == len(Dict) - 1:
        print(sum / len(Dict))