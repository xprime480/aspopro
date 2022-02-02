import os
import sys
import qik

if __name__ == '__main__' :
    total = 512
    path = "./qikqik"

    if len(sys.argv) > 1:
        total = int(sys.argv[1])
    if len(sys.argv) > 2:
        path = sys.argv[2]

    iters = []
    while total > 1:
        x = qik.qik(1, total)
        iters.append(x)
        total //= 2

    l = len(iters)
    for x in range(l-1,0,-1) :
        for i in [max(p[:2]) for p in iters[x]] :
            iters[x-1][i-1].append('*')

    if os.path.exists(path) :
        if os.path.isdir(path) :
            pass
        else :
            raise Exception("path {} exists and is not a directory".format(path))
    else :
        os.mkdir(path)

    idx = 0
    for i,l in enumerate(iters) :
        with open("{}/round{}.txt".format(path,1+i), "w") as fh :
            qik.format(l, fh)
