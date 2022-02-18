import argparse
from operator import le
import ong

def execute_one(length, progressive=False) :
    data = list(range(1, length+1))
    pairs = ong.ong(data[:])
    minval,maxval = length, 0
    vals = []

    for p in pairs :
        diff = abs(data.index(p[0]) - data.index(p[1]))
        vals.append(diff)

        if progressive : 
            data.remove(p[0])
            data.remove(p[1])

    return min(vals), max(vals), sum(vals) / length / 2

def execute(length, progressive, count) :
    if count == 1 :
        return execute_one(length, progressive)

    mins = []
    maxs = []
    avgs = []

    for _ in range(count) :
        mn,mx,av = execute_one(length, progressive)
        mins.append(mn)
        maxs.append(mx)
        avgs.append(av)

    return sum(mins) / count, sum(maxs) / count, sum(avgs) / count

if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description='calculate min and max distance in shuffled sequence')
    parser.add_argument('--length', '-l', default=128, type=int, help='number of items in sequence')
    parser.add_argument('--count', '-c', default=1, type=int, help='number of times to repeat simulation')
    parser.add_argument('--progressive', '-p', default=False, action='store_const', const=True, help='remove items as they are measured')

    args = parser.parse_args()
    ans = execute(args.length, args.progressive, args.count)
    print(ans)
