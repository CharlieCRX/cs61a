'''
    functions as arguments
'''
def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def origin(x):
    ''' this funciton return argument itself
    '''
    return x

def square(x):
    return x*x

def pi_term(k):
    return 8 / ((4*k - 3) * (4*k - 1))

def origin_sum(n):
    return summation(n, origin)

def square_sum(n):
    return summation(n, square)

def pi_sum(n):
    return summation(n, pi_term)
