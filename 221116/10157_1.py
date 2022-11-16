# 갈 곳이 없어서 그 방향으로
# dir 만들어서 가는 방향에 끝나면 방향 돌리기
import sys
C, R = map(int, sys.stdin.readline().rstrip().split())
# C == X, R == Y
num = int(sys.stdin.readline().rstrip())
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
point = [0, 0]
arr = []
ni = 0
nj = -1
d = 0
arr = [[0] * C for _ in range(R)]
for i in range(num + 1):
    ni = ni + dir[d][0]
    nj = nj + dir[d][1]
    arr[ni][nj] = i

    if 0 <= ni + dir[d][0] < R and 0 <= nj + dir[d][1] < C and not arr[ni + dir[d][0]][nj + dir[d][1]]:
        continue
    else:
        if d != 3:
            d += 1
        else:
            d = 0

print(ni, nj)
for i in range(C):
    print(arr[i])
print()
