import sys
import copy
N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().rstrip().split()))
S = list(map(int, sys.stdin.readline().rstrip().split()))
result = [0, 1 ,2] * (N // 3)
cnt = 0
i = 0
while P != result:
    tmp = copy.deepcopy(P)
    for j in range(N):
        P[S[j]] = tmp[j]
    cnt += 1
    print("-1")
    break
else:
    print(cnt)
