
import random

TRACE = False

def solved(puzzle) :
    return puzzle.find('.') < 0

def getrow(pos, item) :
    start = 9 * (pos // 9)
    return set(item[start:start+9])

def getcol(pos, item) :
    start = pos % 9
    return set(item[slice(start,81,9)])

def getblk(pos, item) :
    start = pos - (pos % 3)
    while start not in [0, 3, 6, 27, 30, 33, 54, 57, 60] :
        start -= 9

    return set(item[start:start+3] + item[start+9:start+12] + item[start+18:start+21])

def getlegal(pos, item) :
    return (set('123456789')
        .difference(getrow(pos, item))
        .difference(getcol(pos, item))
        .difference(getblk(pos, item)))

def substitute(new, pos, item) :
    return item[:pos] + new + item[pos+1:]

def getnext(item):
    dot = item.find('.')
    if dot < 0 :
        return []

    totry = list(getlegal(dot, item))
    random.shuffle(totry)
    return [substitute(x, dot, item) for x in totry]

def solutions(puzzle) :
    stack = []
    stack.append(puzzle)
    n = 0

    while stack:
        n += 1
        if TRACE :
            print('Iteration {}, Stack size is {}, progress is {}'.format(n, len(stack), 81 - stack[-1].count('.')))

        item = stack.pop()
        if solved(item) :
            yield item

        next = getnext(item)
        stack.extend(next)

def solve(puzzle) :
    return next(solutions(puzzle), 'Nothing!!'*9)
    
def prettyprint(puzzle) :
    lines = [puzzle[x:x+9] for x in range(0,81,9)]
    for x in range(9):
        if x in [0,3,6] :
            print('| --------------------- |')
        for y in range(9) :
            if y in [0,3,6]:
                print('| ', end='')
            print(lines[x][y], end=' ')
        print('|')
    print('| --------------------- |')


##TESTCASE = '53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79'
##TESTCASE = '123456789' + '.' * 72
TESTCASE = '.' * 81

if __name__ == '__main__' :
    prettyprint(solve(TESTCASE))
