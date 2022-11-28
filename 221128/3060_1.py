import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    total = 0
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    N -= sum(arr)
    if N >= 0:
        for i in range(6):
            chk = [i - 1, i, i + 1, i + 3]
            for j in range(len(chk)):
                if 0 <= chk[j] < 6:
                    total += arr[chk[j]]
                elif chk[j] < 0:
                    total += arr[chk[j] + 5]
                else:
                    total += arr[chk[j] - 6]
    

    print(total)