def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last

def fact_iter(n):
    total, k = 1, 1
    while k < n:
        total, k = total * k, k + 1
    return total

def fact_recuresive(n):
    if n == 1:
        return 1
    else:
        return n * fact_recuresive(n - 1)
    
def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)

def is_even_recursive(n):
    if n == 0:
        return True
    if n == 1:
        return False
    
    return is_even_recursive((n - 1) - 1)

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

def play_alice(n):
    if n == 0:
        print('Bob wins!')
    else:
        play_bob(n - 1)

def play_bob(n):
    if n == 0:
        return print('Alice wins!')
    elif is_even(n):
        play_alice(n - 2)
    else:
        play_alice(n -1)

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    
    return count_partitions(n-m, m) + count_partitions(n, m -1)