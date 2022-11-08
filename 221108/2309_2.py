import sys
arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
all = sum(arr)
idxI = 0
idxJ = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if all - arr[i] - arr[j] == 100:
            idxI = i
            idxJ = j
            break
arr[idxI] = 100
arr[idxJ] = 100
for i in range(9):
    if arr[i] < 100:
        print(arr[i])