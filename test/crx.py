def summation(n, term):
    total,k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total