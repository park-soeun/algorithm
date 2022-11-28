import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    total = 0
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    N -= sum(arr)
    chk = [[5, 1, 3], [0, 2, 4], [1, 3, 5], [2, 4, 0], [3, 5, 1], [4, 0, 2]]
    cnt = 1
    while N >= 0:
        cnt += 1
        for i in range(6):
            chk = [i - 1, i, i + 1, i + 3]
            for j in range(len(chk)):
                if 0 <= chk[j] < 6:
                    N -= arr[chk[j]]
                elif chk[j] < 0:
                    N -= arr[chk[j] + 5]
                else:
                    N -= arr[chk[j] - 6]
    
    

    print(cnt)