import sys
import ong

def qik(start, stop) :
    v0 = [x for x in range(start,stop+1)]
    return ong.ong(v0)

def format(data, fh=sys.stdout) :
    for v in data:
        if len(v) == 2 :
            fmt = "({}, {})\n"
        elif len(v) == 3 :
            fmt = "({}, {}) {}\n"
        else:
             fmt = "?? {}"
        fh.write(fmt.format(*v))

if __name__ == '__main__' :
    start = 1
    stop = 170

    if len(sys.argv) > 1:
        stop = int(sys.argv[1])
    if len(sys.argv) > 2:
        start = int(sys.argv[2])

    v1 = qik(start, stop)
    format(v1)
