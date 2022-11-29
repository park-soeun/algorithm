import sys
N = int(sys.stdin.readline().rstrip())
arr = [[0] * (N + 2)]
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip()))
    tmp = [0] + tmp + [0]
    arr.append(tmp)
arr.append([0] * (N + 2))
k = 1
tmp_num = 1
cnt = 0
ans = []
tmpp = []
for i in range(N + 1):
    for j in range(N + 1):
        if arr[i][j] != 0:
            tmp_num += 1    
            print()
            tmpp = [[i, j]]
            k = 0
            for d in range(4):
                
                while k < N - 1:
                    dir = [[0, k], [k, 0], [0, -k], [-k, 0]]
                    k += 1
                    ni = i + dir[d][0]
                    nj = j + dir[d][1]
                    print(ni, nj)

                    if arr[ni][nj] != 0 and [ni, nj] not in tmpp:
                        tmpp.append([ni, nj])
                        arr[ni][nj] = tmp_num
                        if arr[ni][nj] == 0:
                            break
        print(i, j, tmpp)
            
                
    
for i in range(N + 2):
    print(arr[i])

        # if arr[i][j] == tmp_num:
        #     arr[i][j] = tmp_num + 1
        # if arr[i][j] == tmp_num + 1:

            

