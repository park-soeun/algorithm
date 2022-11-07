import sys
T = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
for i in range(T):
    for j in range(i + 1, T):
        if arr[i] < arr[j]:
            print(arr[j], end=" ")
            break
    else:
        print("-1", end=" ")
            