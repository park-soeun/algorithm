import sys
N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
cnt = 0
dasom = arr[0]
candi = arr[1:]

if len(candi) == 0:
    cnt = 0
else:
    max_candi = max(candi)
    while dasom <= max_candi:
        for i in range(len(candi)):
            if candi[i] >= dasom:
                print(dasom, candi)
                candi[i] -= 1
                dasom += 1
                cnt += 1
                max_candi = max(candi)
            max_candi = max(candi)
print(dasom, candi)
print(cnt)