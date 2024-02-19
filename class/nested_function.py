def improve(close, update, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def average(a, b):
    return (a + b) / 2

def approx_eq(a, b, tolerance = 1e-10):
    return abs(a - b) < tolerance

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x*x, a)
    return improve(sqrt_close, sqrt_update)
    