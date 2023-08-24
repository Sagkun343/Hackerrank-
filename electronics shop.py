def getMoneySpent(keyboards, drives, b):
    moni = 0
    for i in range(len(keyboards)):
        for k in range(len(drives)):
            if (keyboards[i]+drives[k])<= b and (keyboards[i]+drives[k])>moni:
                moni = keyboards[i]+drives[k]
    if moni == 0:
        return -1
    else:
        return moni