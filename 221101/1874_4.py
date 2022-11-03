import sys

n = int(sys.stdin.readline().rstrip())
arr = []
arr2 = []
tmp = []
result = []
ele = 1
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
for j in range(n):
    while ele < n+1:
        if len(tmp) > 0:
            if tmp[-1] == arr[j]:
                arr2.append(tmp.pop())
                result.append('-')
                break
            elif tmp[-1] < arr[j]:
                tmp.append(ele)
                ele += 1
                result.append('+')
            else:
                arr2.append(tmp.pop())
                result.append('-')
        else:
            if arr[j] == ele:
                tmp.append(ele)
                ele += 1
                result.append('+')
                arr2.append(tmp.pop())
                result.append('-')
            
                break
            else:
                tmp.append(ele)
                ele += 1
                result.append(f'+')
print(f'arr {arr}')
print(f'arr2 {arr2}')
print(f'tmp {tmp}')
for j in range(len(tmp)):
    arr2.append(tmp.pop())
    result.append('-')
if arr == arr2:
    for i in range(len(result)):
        print(result[i])
else:
    print('NO')

print(arr, arr2)