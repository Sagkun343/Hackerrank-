def utopianTree(n):
    tree_height = 1
    for i in range(1,n+1):
        if i % 2 == 1:
            tree_height *= 2
        else:
            tree_height += 1
    return tree_height