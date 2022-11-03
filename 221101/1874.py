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
        print(f'+ {ele}' )
        ele += 1
    elif arr[j] == ele:
        tmp.append(ele)
        arr2.append(tmp.pop())
        print('-pop')
        break
    else:
        arr2.append(tmp.pop())
        print('-else')
        break

