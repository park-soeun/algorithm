import sys

n = int(sys.stdin.readline().rstrip())
arr = []
arr2 = []
tmp = []
ele = 1
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

for j in range(n):
    if arr[j] > ele:
        tmp.append(ele)
        ele += 1
        print('+')
    else:
        if tmp[-1] == arr[j]:
            arr2.append(tmp.pop())
            print('-')
            print(ele)
        else:
            print('error')
