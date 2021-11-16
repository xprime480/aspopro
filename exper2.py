import itertools as it
from operator import mul
from functools import reduce

def convert(it) :
    l = [][:]
    for x in range(0, len(it), 2) :
        vals = it[x:x+2]
        l.append(frozenset(vals))
    return frozenset(l)

def gen(data) :
    q = set()
    for p in it.permutations(data) :
        s = convert(list(p))
        q.add(s)
    return q

def count(sets) :
    n = 0
    for s in sets :
        for p in s :
            if 1 == max(p) - min(p) :
                n += 1
                break

    return n, len(sets)

def run(n) :
    data = list(range(1, n+1))
    q = gen(data)
    match,total = count(q)
    print(n, match, total)

def m1() :
    for n in range(2, 13, 2) :
        run(n)

__memo__ = [1, 0]
def f(n) :
    if n < 0 :
        return 0

    if n < len(__memo__) :
        return __memo__[n]

    for x in range(len(__memo__), n+1) :
       __memo__.append(__memo__[x-2] * (x-1))

    return __memo__[n]

def count2(data) :
    if len(data) == 2 :
        if abs(data[0]-data[1]) == 1 :
            return 1, 1
        return 0, 1

    m = 0
    a = min(data)
    d2 = data[:]
    d2.remove(a)

    for d in d2 :
        if 1 == (d - a) :
            m += f(len(d2)-1)
        else :
            d3 = d2[:]
            d3.remove(d)
            m += count2(d3)[0]

    return m, f(len(data))

def run2(n) :
    data = list(range(1, n+1))
    match, total = count2(data)
    print(n, match, total)

def m2() :
    for n in range(2, 21, 2) :
        run2(n)

#m1()
m2()