def climbingLeaderboard(ranked):
    rank = 1
    arr2 = [1]
    for i in range(1,len(ranked)):
        if ranked[i] == ranked[i-1]:
            arr2.append(rank)
        else:
            rank +=1
            arr2.append(rank)
    return arr2

print(climbingLeaderboard([100, 90 , 90 , 80]))