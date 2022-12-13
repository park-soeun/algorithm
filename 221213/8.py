import sys

T = int(sys.stdin.readline().rstrip())
for tc in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    prefix_sum = [0]
    result = 0
    for i in range(N):
        total = arr[i]
        finish = 0
        minus = []

        for j in range(i + 1, N):
            tmp1 = 0
            tmp2 = 0
            cnt1 = 0
            cnt2 = 0
            if arr[j] < 0:
                finish = 1
                if arr[j] < 0 and cnt2 == 0:
                    tmp1 += arr[j]
                    minus.append(arr[j])
                    cnt1 += 1
                elif arr[j] >= 0:
                    tmp2 += arr[j]
                    cnt2 += 1
                else:
                    if tmp1 > tmp2:
                        break
                    else:
                        total += tmp1 + tmp2
                        finish = 0
            elif arr[j] >= 0 and finish == 0:
                total += arr[j]


        finish = 0
        for j in range(i - 1, -1, -1):
            tmp1 = 0
            tmp2 = 0
            cnt1 = 0
            cnt2 = 0
            if arr[j] < 0:
                finish = 1
                if arr[j] < 0 and cnt2 == 0:
                    tmp1 += arr[j]
                    cnt1 += 1
                elif arr[j] >= 0:
                    tmp2 += arr[j]
                    cnt2 += 1
                else:
                    if tmp1 > tmp2:
                        break
                    else:
                        total += tmp1 + tmp2
                        finish = 0
            elif arr[j] >= 0 and finish != 1:
                total += arr[j]

        print(total)
        if len(minus) > 0:        
            mini = min(minus)
            
            total -= mini
        result += total
        result = result % 1000000007
        ans1 = str('#')
        ans2 = str(tc+1)
        ans3 = str(result)
        ans = str('#{tc+1}')
        ans = '#'
        ans += ans2
        ans += ' '
        ans += ans3
    print(ans)
    

    
                

            
            



            
                

            


        # for q in range(0, i):

        


