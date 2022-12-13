import sys

T = int(sys.stdin.readline().rstrip())
for tc in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    con = []
    prefix_sum = [0]
    for i in range(N):
        prefix_sum = [0]
        tmp = 0
        for j in range(i + 1, N):
            tmp += arr[j]
            prefix_sum.append(tmp)
        print(prefix_sum)
    
                

            
            



            
                

            


        # for q in range(0, i):

        


