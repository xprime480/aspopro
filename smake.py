import random
import ssolve

#
# the following algorithm generates lousy puzzles 
# and may even admit of the possibility of an 
# infinite loop.  but it has worked "so far"
#
def gen() :
    stack = ['.' * 81]
    x = 0

    while stack :
        puzzle = stack.pop()

        while True :
            x = random.randint(0, 80)
            if puzzle[x] == '.' :
                break

        choices = ssolve.getlegal(x, puzzle)
        for c in choices :
            next = ssolve.substitute(c, x, puzzle)
            stack.append(next)

        while True :
            puzzle = stack.pop()

            solns = [x for _,x in zip(range(2), ssolve.solutions(puzzle))]
            if len(solns) == 0 :
                # the current candidate is inconsistent, continue
                pass
            elif len(solns) == 1 :
                # exactly one solution, a good candidate
                return puzzle
            else :
                # this one has multiple solutions, continue
                stack.append(puzzle)
                break

def genfrom(puzzle) :
    # end recursion, check if we found a valid solution
    #
    if puzzle.count('.') == 81-17 :
        solns = [x for _,x in zip(range(2), ssolve.solutions(puzzle))]
        if len(solns) == 1 :
            return puzzle
        else :
            print('bottomed out unsuccessfully with {}'.format(puzzle))
            return None

    # we can remove at least one item, so recurse over each possibility
    # until one is found
    indexes = list(range(81))
    random.shuffle(indexes)
    for x in indexes:
        if puzzle[x] != '.' :
            next = ssolve.substitute('.', x, puzzle)

            solns = [x for _,x in zip(range(2), ssolve.solutions(next))]
            if len(solns) == 1 :
                # exactly one solution, this one maybe could get shorter
                test = genfrom(next)
                if test :
                    return test
            else :
                # this one is ambiguous or inconsistent, skip it
                print('ambiguity with {}'.format(next))
                pass

    return None

def dotify(puzzle, indexes) :
    next = ['.'] * 81

    for x in range(81) :
        if x not in indexes :
            next[x] = puzzle[x]

    return ''.join(next)

def genfrom2(puzzle) :
    indexes = list(range(81))
    while True :
        random.shuffle(indexes)
        next = dotify(puzzle, indexes[:64])
        solns = [x for _,x in zip(range(2), ssolve.solutions(next))]
        if len(solns) == 1 :
            # exactly one solution, winner!
            return next

#
# supposedly better algorithm.  start with a completed puzzle
# and remove until you can't remove any more.  min length is 17.
#
def gen2() :
    puzzle = [x for _,x in zip(range(1), ssolve.solutions('.' * 81))][0] ## start with any puzzle
    return genfrom2(puzzle)

if __name__ == '__main__' :
    #ssolve.prettyprint(gen())
    ssolve.prettyprint(gen2())