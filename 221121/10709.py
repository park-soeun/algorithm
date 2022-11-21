import sys
H, W = map(int, sys.stdin.readline().rstrip().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
paper = [[-1] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'c':
            paper[i][j] = 0
        if paper[i][j] == 0:
            for k in range(1, W):
                if j + k < W:
                    paper[i][j + k] = paper[i][j + k - 1] + 1
                else:
                    break
            
for i in range(H):        
    print(*paper[i])



