import sys
N = int(sys.stdin.readline().rstrip())
arr = [[0] * (N + 2)]
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip()))
    tmp = [0] + tmp + [0]
    arr.append(tmp)
arr.append([0] * (N + 2))

tmpp = []
tmp_num = 1
for i in range(N + 2):
    for j in range(N + 2):
        if arr[i][j] == 1:
            tmpp.append([i, j])

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
ans = True
tmppp = []
for i in range(len(tmpp)):
    if tmpp[i] not in tmppp:
        
        tmppp.append(tmpp[i])
        new_tmp = [tmpp[i]]
    while ans:
        for p in range(len(new_tmp)):
            cnt = 0
            for d in range(4):
                ni = new_tmp[p][0] + dir[d][0]
                nj = new_tmp[p][1] + dir[d][1]
                if [ni, nj] in tmpp and [ni, nj] not in new_tmp:
                    tmppp.append([ni, nj])
                    new_tmp.append([ni, nj])
                    cnt += 1
        if cnt == 0:
            ans = False
            print(new_tmp)
            new_tmp = []
            
        

                
               
        