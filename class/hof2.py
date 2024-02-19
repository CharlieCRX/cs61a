def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def cube(x):
    return x*x*x

def identity(x):
    return x

def sum_cubes(n):
    return summation(n, cube)

def sum_naturals(n):
    return summation(n, identity)