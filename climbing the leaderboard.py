
import math
import os
import random
import re
import sys


def climbingLeaderboard(ranked, player):
    l1 = []
    val = -1
    for i in range(len(ranked)):
        if ranked[i] != val:
            val = ranked[i]
            l1.append(ranked[i])
    rank = 1
    l2 = []
    for k in range(len(player)):
        l3 = l1
        if player[k] in l3:
            l2.append(l3.index(player[k])+1)
        else:
            l3.append(player[k])
            l3 = sorted(l3)
            l2.append(l3.index(player[k])+1)
    return l2


climbingLeaderboard([100,100,50,40,40,20,10],[5,25,50,120])


