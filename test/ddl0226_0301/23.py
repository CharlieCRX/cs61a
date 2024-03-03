'''
    The implementation of the linked list is based on 
    python's built-in list type, 
    which can be changed to custom class data in the future 
    to achieve an abstract barrier.
'''
    #about linklist start at 2024.2.28 17:30
empty = 'empty'
def is_link(s):
    if s == empty:
        return True
    return len(s) == 2 and is_link(s[1])

def link(first, rest):
    assert is_link(rest),'rest must be a list'
    return [first, rest]

def first(s):
    '''返回链表的第一个元素'''
    assert is_link(s), 'first只能用于链表'
    assert s != empty, '空链表没有第一个元素'
    return s[0]

def rest(s):
    '''返回链表的剩余元素'''
    assert is_link(s), 'rest只能用于链表'
    assert s != empty, '空链表没有剩余元素'
    return s[1]


def len_link(s):
    '''返回链表 s 的长度'''
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length


def getitem_link(s, i):
    '''获取链表索引位置为i的值域;索引从0开始'''
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

four = [1, [2, [3, [4, 'empty']]]]


def len_link_recursive(s):
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    """返回链表 s 中索引为 i 的元素"""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)

def extend_link(s, t):
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    
    return link(first(s), extend_link(rest(s), t))


def apply_to_all_link(f, s):
    assert is_link(s)
    if s == empty:
        return s
    return link(f(first(s)), apply_to_all_link(f, rest(s)))

def keep_if_link(f, s):
    """难：返回 s 中 elem 被 f 作用时， 为 True 的元素"""
    assert is_link(s)
    if s == empty:
        return s
     
    kept = keep_if_link(f, rest(s))
    if f(first(s)):
        return link(first(s), kept)
    else:
        return kept
def join_link(s, separator):
        """返回由 separator 分隔的 s 中的所有元素组成的字符串"""
        if s == empty:
            return ""
        elif rest(s) == empty:
            return str(first(s))
        else:
            return str(first(s)) + separator + join_link(rest(s), separator)
def mutable_link():
    """返回一个可变链表的函数"""
    contents = empty
    def dispatch(message, value = None):
        nonlocal contents
        if message == 'len':
            return len_link(contents)
        elif message == 'getitem':
            return getitem_link(contents, value)
        elif message == 'push_first':
            contents = link(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return join_link(contents, ", ")
        
    return dispatch

def to_mutable_link(source):
    s = mutable_link()
    for elem in reversed(source):
        s('push_first', elem)
    return s
suits = ['heart', 'diamond', 'spade', 'club']
s = to_mutable_link(suits)
        

    #about linklist start