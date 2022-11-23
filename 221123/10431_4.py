import sys
P = int(sys.stdin.readline().rstrip())
for _ in range(P):
    cnt = 0
    result = []
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    num = arr[:1]
    arr = arr[1:]
    result.append(arr[0])
    arr.pop(0)
    for i in range(19):
        for j in range(len(result)):
            
            if arr[i] > result[-1]:
                result.append(arr[i])
                break
            elif arr[i] > result[j] and arr[i] < result[j + 1]:
                result.insert(j + 1, arr[i])
                cnt += (len(result) - j - 2)
                break
            elif min(result) > arr[i]:
                result.insert(0, arr[i])
                cnt += (len(result) - 1)
            
    print(*num, end=" ")
    print(cnt)
