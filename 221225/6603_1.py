import sys

def dfs(idx, list):
    
    if len(list) == r:
        answer.append(list[:])
        
    for i in range(idx, len(S)):
        dfs(i + 1, list + [S[i]])



while True:
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    if arr[0] != 0:
        k = arr[0]
        S = arr[1:]
        answer = []
        r = 6
        dfs(0, [])
        for i in range(len(answer)):
            print(*answer[i])
        print()
    else:
        break