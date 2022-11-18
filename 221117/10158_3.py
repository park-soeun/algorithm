import sys
w, h = map(int, sys.stdin.readline().rstrip().split())
p, q = map(int, sys.stdin.readline().rstrip().split())
t = int(sys.stdin.readline().rstrip())

# Q 가 H 임 

# print(t // h)
if ((p + t) // w) % 2 == 0:
    p = (p + t) % w
    print("짝")
else:
    p = w - (p + t) % w
    print("홀")

if ((q + t) // h) % 2 == 0:
    q = (q + t) % h
    print("짝")
else:
    q = h - (q + t) % h
    print("홀")


# q = q - t // h * h + t % h
# p = p - t // w * w + t % w
# print(t // w * w)
# print(t % w)


print(p, q)