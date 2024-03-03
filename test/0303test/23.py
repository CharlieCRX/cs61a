from operator import add


def divisors1(n):
    '''输入n,获取n的公约数,并且将结果放入集合中'''
    return [1] + [x for x in range(2, n) if n % x == 0]

def perfect1(n):
    return sum(divisors1(n)) == n

a1 = [x for x in range(1, 1000) if perfect1(x)]

'''
    序列抽象之：高阶函数。
    apply_to_all(map_fn, s):将对序列s中每个元素进行表达式求值并返回结果序列
    keep_if(filter_fn, s):筛选序列s中符合条件filter_fn的值
    reduce(reduce_fn, s, inital):双参数函数reduce_fn重复作用到每个元素和初始值
    应用：
    divisors_of(n):利用高阶函数获取n的公约数
    sum_of_divisors(n):公约数的和
    perfect(n):完美数
    利用keep_if(filter_fn, s)获取1-1000范围内的完美数
'''

def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, inital):
    reduced = inital
    for x in s:
        reduced = reduce_fn(x, reduced)
    return reduced

a2 = [-1, -2, -3, -4, 5]

a21 = apply_to_all(abs, a2)

a22 = keep_if(lambda y: y > 0, a2)

a23 = keep_if(lambda y: y > 0, a21)

a24 = reduce(add, a2, 0)

def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

def sum_of_divisors2(n):
    return sum(divisors_of(n))

def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)

def is_perfect(n):
    return sum_of_divisors(n) == n
a25 = [x for x in range(1, 1000) if is_perfect(x)]

'''
    tree...
'''
def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch),'分支必须是树'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

t = [3, [1], [2, [1], [1]]]

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    left, right = fib_tree(n -2), fib_tree(n - 1)
    fib_n = label(left) + label(right)
    return tree(fib_n, [left, right])

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    branch_counts = [count_leaves(b) for b in branches(tree)]
    return sum(branch_counts)
