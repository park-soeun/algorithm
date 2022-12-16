import sys
num = list(map(int, sys.stdin.readline().rstrip().split()))
stk = []
sorted_num = sorted(num)
ans = sorted_num[0] * 1000 + sorted_num[1] * 100 + sorted_num[2] * 10 + sorted_num[3]
tmp = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1 ,10):
            for d in range(1, 10):
                tmp = [a * 1000 + b * 100 + c * 10 + d, b * 1000 + c * 100 + d * 10 + a, c * 1000 + d * 100 + a * 10 + b, d * 1000 + a * 100 + b * 10 + c] 
                check = min(tmp) 
                if check not in stk:        
                    stk.append(check)

for i in range(30):
    # if stk[i] == ans:
    #     print(i)
    #     break
    print(stk[i])
