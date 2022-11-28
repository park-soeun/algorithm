import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
result = ['?'] * N
arr = [list(sys.stdin.readline().rstrip().split()) for _ in range(K)] 
# print(arr)
idx = 0

for i in range(K):
    idx += int(arr[i][0])
    txt = arr[i][1]

    while idx < N:
        if result[idx] == '?' or result[idx] == txt:
            result[idx] = txt
            break
        else:
            print('!')
            break
    else:
        idx -= N
        if result[idx] == '?' or result[idx] == txt:
            result[idx] = txt
            break
        else:
            print('!')
            break



print(*result)