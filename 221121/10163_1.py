import sys
N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# for i in range(N):
    # arr = list(map(int, sys.stdin.readline().rstrip().split()))
paper = [[999] * 1001 for _ in range(1001)]
result = []
minus = []
for i in range(N):
    p = arr[i][0]
    q = arr[i][1]
    width = arr[i][2]
    height = arr[i][3]
    tmp = 0
    for x in range(p, p + width):
        for y in range(q, q + height):
            paper[x][y] = i   
            # 빼는 거로 해도 되겠다.. 

for k in range(N):
    cnt = 0
    for i in range(101):
        for j in range(101):
            if paper[i][j] == k:
                cnt += 1
    print(cnt)