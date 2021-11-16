import sys
import ong

stop = 170
start = 1
if len(sys.argv) > 1:
    stop = int(sys.argv[1])
if len(sys.argv) > 2:
    start = int(sys.argv[2])

v0 = [x for x in range(start,stop+1)]
v1 = ong.ong(v0)
for v in v1:
    print(v[0], v[1])
