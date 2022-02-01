import sys
import qik

if __name__ == '__main__' :
    total = 512

    if len(sys.argv) > 1:
        total = int(sys.argv[1])

    iters = []
    while total > 1:
        x = qik.qik(1, total)
        iters.append(x)
        total //= 2

    l = len(iters)
    for x in range(l-1,0,-1) :
        for i in [max(p[:2]) for p in iters[x]] :
            iters[x-1][i-1].append('*')

    idx = 0
    subdir = "qikqik"
    for i,l in enumerate(iters) :
        with open("./qikqik/round{}.txt".format(1+i), "w") as fh :
            qik.format(l, fh)
