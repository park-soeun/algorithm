import sys

T = int(sys.stdin.readline().rstrip())
for tc in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    result = 0
    for i in range(N):
        total = arr[i]
        if i + 1 < N:
            p = i + 1
            while arr[p] >= 0:
                total += arr[p]
                p += 1
            else:
                tmp1 = 0
                tmp2 = 0
                while arr[p] < 0 :
                    tmp1 += arr[p]
                    p += 1
                else:
                    while arr[p] >= 0:
                        tmp2 += arr[p]
                        p += 1
                print(tmp1, tmp2)

            
            



            
                

            


        # for q in range(0, i):

        


