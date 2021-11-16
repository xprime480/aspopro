import sys
import ong

def items_from_line(line) :
    line = line.strip()
    if len(line) < 5:
        return []
    if line[0] is not '(' or line[-1] is not ')' :
        return []

    line = line[1:-1]
    try :
        return [int(x.strip()) for x in line.split(',')]
    except:
        return []


def get_array_from_file(fname) :
    inputs = []
    with open(fname, 'r') as fh:
        for l in fh.readlines() :
            inputs.extend(items_from_line(l))
    return inputs

if __name__ == "__main__" :
    if len(sys.argv) <= 1:
        print("File name is required")
        exit(1)

    v0 = get_array_from_file(sys.argv[1])
    v1 = ong.ong(v0)
    for v in v1:
        print(v[0], v[1])
