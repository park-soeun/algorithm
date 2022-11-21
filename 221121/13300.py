import sys
arr = list(map(int, sys.stdin.readline().rstrip().split()))
answer = [1, 2, 3, 4, 5]
i = 0
while arr != answer:
    if i < 4:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(*arr)
        i += 1
    else:
        i = 0