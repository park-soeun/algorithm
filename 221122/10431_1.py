import sys
P = int(sys.stdin.readline().rstrip())
for _ in range(P):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr = arr[1:]
    print(arr)