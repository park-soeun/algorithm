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
        tmp_arr = [0] * 6
        for j in range(6):
            tmp = 0
            tmp += arr[chk[j][0]] + arr[chk[j][1]] + arr[chk[j][2]] + arr[j]
            N -= tmp
            tmp_arr[j] = tmp
        arr = tmp_arr
        
    print(cnt)