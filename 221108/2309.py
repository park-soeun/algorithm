import sys
arr = []
all = 0
for i in range(9):
    arr.append(int(sys.stdin.readline().rstrip()))
for i in range(9):
    all += arr[i]
arr.sort()
out = []
for i in range(9):
    for j in range(i + 1, 9):
        if all - arr[i] - arr[j] == 100:
            out.append(i)
            out.append(j)
            break
result = []
for i in range(9):
    if i not in out:
        result.append(arr[i])
    
for ele in result:
    print(ele)

