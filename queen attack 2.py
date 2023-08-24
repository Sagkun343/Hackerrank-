def queensAttack(n, k, r_q, c_q, obstacles):
    d_1 = 2*(n-1)
    row = r_q
    coloumn = c_q
    while row<n and coloumn<n:
        row += 1
        coloumn += 1
        d_1 += 1
    while 