import sys

T = int(sys.stdin.readline().rstrip())
for tc in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    result = 0
    for i in range(N):
        total = arr[i]
        # 여기서 인덱스 에러 날 수 있음
        for p in range(i + 1, N):
            tmp1 = 0
            tmp2 = 0
            if arr[p] >= 0:
                total += 1
            else:
                if p == N - 1:
                    break
                else:

        for q in range(0, i):

        


