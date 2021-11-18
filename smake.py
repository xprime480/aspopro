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

if __name__ == '__main__' :
    ssolve.prettyprint(gen())