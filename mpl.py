import sys

def kill_last_char(fname) :
    with open(fname) as fh:
        x = fh.read()

    if len(x) :
        with open(fname, 'w') as fh :
            fh.write(x[:-1])

if __name__ == '__main__' :
    for f in sys.argv[1:] :
        kill_last_char(f)