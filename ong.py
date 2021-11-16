import numpy.random

def ong(v0, sz=2) :
    numpy.random.shuffle(v0)
    v1 = [(v0[sz*i:sz*i+sz]) for i in range(len(v0) // sz)]
    v1.sort(key=lambda x: max(x))
    return v1