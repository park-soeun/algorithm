import sys
P = int(sys.stdin.readline().rstrip())
for _ in range(P):
    cnt = 0
    result = []
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr = arr[1:]
    result.append(arr[0])
    arr.pop(0)
    for i in range(19):
        if result[0] > arr[i]:
            result.insert(0, arr[i])
            cnt += len(result)
        else:
            
            for j in range(len(result) - 1):
                if arr[i] > result[j] and arr[i] < result[j + 1]:
                    cnt += 1
                    print('바보1')
                else:
                    print('바보양')
                    
    print(f'result = {result}')
    print(f'cnt = {cnt}')
