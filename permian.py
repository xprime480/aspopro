
import random
import functools
import operator
import collections

def factorial(n) :
    return functools.reduce(operator.mul, range(1, n+1), 1)

def kth_permutation(N, k) :
    Fs = list(map(factorial, range(N+1)))
    i = k-1
    p = []
    v = list(range(1,N+1))
    x = i
    for j in list(reversed(Fs[1:-1])) :
        y = x // j
        x = x % j
        c = v[y]
        p.append(c)
        v.remove(c)
    p.extend(v)

    return p

def random_permutation(N) :
    upper = factorial(N)
    k = random.randint(1, upper+1)
    return kth_permutation(N, k)

def all_permutations(N) :
    for i in range(1, 1+factorial(N)) :
        yield(kth_permutation(N, i))

if __name__ == '__main__' :
    for p in all_permutations(4) :
        print(p)
    
    def maxd(N) :
        base = kth_permutation(N, 1)
        for p in all_permutations(N) :
            yield max([abs(a-b) for a, b in zip(p, base)])

    print(collections.Counter(maxd(10)))
