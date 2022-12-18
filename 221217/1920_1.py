import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort()
answer = []

for i in range(M):
    lower = 0
    upper = N - 1
    ans = 0
    while lower <= upper:
        middle = (lower + upper) // 2
        if A[middle] == arr[i]:
            ans = 1
            break
        elif A[middle] > arr[i]:
            upper = middle - 1
        else:
            lower = middle + 1
            
    answer.append(ans)
    
print(*answer, sep='\n')