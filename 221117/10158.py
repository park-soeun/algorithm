import sys
w, h = map(int, sys.stdin.readline().rstrip().split())
p, q = map(int, sys.stdin.readline().rstrip().split())
t = int(sys.stdin.readline().rstrip())

if ((p + t) // w) % 2 == 0:
    p = (p + t) % w
else:
    p = w - (p + t) % w

if ((q + t) // h) % 2 == 0:
    q = (q + t) % h
else:
    q = h - (q + t) % h


print(p, q)