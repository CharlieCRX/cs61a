def improve(upadte, close, guess = 1):
    while not close(guess):
        guess = upadte(guess)
    return guess

def golden_update(guess):
    return 1 + 1/guess

def square_close_to_successor(guess):
    return approx_eq(guess*guess, guess + 1)

def approx_eq(a, b, tolerance = 1e-15):
    return abs(a - b) < tolerance

phi = improve(golden_update, square_close_to_successor)