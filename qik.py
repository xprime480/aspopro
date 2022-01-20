import sys
import ong

def qik(start, stop) :
    v0 = [x for x in range(start,stop+1)]
    return ong.ong(v0)

if __name__ == '__main__' :
    start = 1
    stop = 170

    if len(sys.argv) > 1:
        stop = int(sys.argv[1])
    if len(sys.argv) > 2:
        start = int(sys.argv[2])

    v1 = qik(start, stop)
    for v in v1:
        ##print(v[0], v[1])
        print("({}, {})".format(*v))
