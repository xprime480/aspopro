
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
    legal = set('123456789')
    legal.difference_update(getrow(pos, item))
    legal.difference_update(getcol(pos, item))
    legal.difference_update(getblk(pos, item))
    return legal

def substitute(new, pos, item) :
    return item[:pos] + new + item[pos+1:]

def getnext(item):
    dot = item.find('.')
    if dot < 0 :
        return []

    totry = getlegal(dot, item)
    return [substitute(x, dot, item) for x in totry]

def solve(puzzle) :
    stack = []
    stack.append(puzzle)
    n = 0

    while stack:
        n += 1
        print('Iteration {}, Stack size is {}'.format(n, len(stack)))
        item = stack.pop()
        if solved(item) :
            return item

        next = getnext(item)
        stack.extend(next)

    return 'Nothing!!'*9

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
TESTCASE = '123456789' + '.' * 72

if __name__ == '__main__' :
    prettyprint(solve(TESTCASE))