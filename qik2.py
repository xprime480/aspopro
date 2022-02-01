import sys
import ong

def qik(start, stop) :
    v0 = [x for x in range(start,stop+1)]
    return ong.ong(v0)

if __name__ == '__main__' :
    total = 512

    if len(sys.argv) > 1:
        total = int(sys.argv[1])

    iters = []
    while total > 1:
        x = qik(1, total)
        iters.append(x)
        total //= 2

    l = len(iters)
    for x in range(l-1,0,-1) :
        for i in [max(p[:2]) for p in iters[x]] :
            iters[x-1][i-1].append('*')

    print(iters)
