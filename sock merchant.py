def sockMerchant(n, ar):
    sock_dict = dict()
    pair = 0
    for i in range(n):
        if ar[i] not in sock_dict:
            sock_dict[ar[i]] = 1
        else:
            sock_dict[ar[i]] += 1
    for key in sock_dict:
        pair += sock_dict[key]//2
    return pair
print(sockMerchant(7, [2,3,4,5,2,3,4]))
