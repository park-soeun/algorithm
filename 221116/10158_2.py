import sys
w, h = map(int, sys.stdin.readline().rstrip().split())
p, q = map(int, sys.stdin.readline().rstrip().split())
t = int(sys.stdin.readline().rstrip())
a = 1
b = 1
for _ in range(1, t + 1):
    q = q + a
    p = p + b
    if q == 0 or q == h:
        a = -a
    if p == 0 or p == w:
        b = -b
print(p, q)