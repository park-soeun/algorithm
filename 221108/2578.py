import sys
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(5)]
num = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        print(i, j)
        print(j, i)
