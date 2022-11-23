import sys
P = int(sys.stdin.readline().rstrip())
result = []
for _ in range(P):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr = arr[1:]
    for i in range(20):
        
        result.append(arr[i])