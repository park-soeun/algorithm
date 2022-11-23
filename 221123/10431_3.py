import sys
P = int(sys.stdin.readline().rstrip())
for _ in range(P):
    cnt = 0
    result = []
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    num = arr[:1]
    arr = arr[1:]
    
    for i in range(20):
        if len(result) == 0:
            result = [arr[i]]
            
            
        else:
            for j in range(len(result)):
                if arr[i] < result[j]:
                    result.insert(j + 1, arr[i])
                    cnt += (len(result) - j - 1)
                    break
                    
                else:
                    result.insert(j, arr[i])
                    break
                    
    # print(f'result = {result}')
    # print(*num, end=" ")
    print(cnt)
