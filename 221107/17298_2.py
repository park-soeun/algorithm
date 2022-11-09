import sys
T = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
tmp = []
stk = []
for i in range(T):
    j = i
    stk.append(arr[i])
    while j < T:
        if stk[i] < arr[j]:
            stk.append(arr[j])
        else:
            tmp.append(arr[j])
            j += 1
    else:
        stk.append("-1")
print(stk[1], end=" ")

