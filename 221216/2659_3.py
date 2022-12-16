import sys
num = list(map(int, sys.stdin.readline().rstrip().split()))
stk = []

ans = num[0] * 1000 + num[1] * 100 + num[2] * 10 + num[3]
a = ans // 1000
b = ans // 100 - a * 10
c = ans // 10 - a * 100 - b * 10
d = ans // 1 - a * 1000 - b * 100 - c * 10

tmp = [a * 1000 + b * 100 + c * 10 + d, b * 1000 + c * 100 + d * 10 + a, c * 1000 + d * 100 + a * 10 + b, d * 1000 + a * 100 + b * 10 + c] 
ans = min(tmp)

tmp = 0
for i in range(1, 10000):
    a = i // 1000
    b = i // 100 - a * 10
    c = i // 10 - a * 100 - b * 10
    d = i // 1 - a * 1000 - b * 100 - c * 10
    
    tmp = [a * 1000 + b * 100 + c * 10 + d, b * 1000 + c * 100 + d * 10 + a, c * 1000 + d * 100 + a * 10 + b, d * 1000 + a * 100 + b * 10 + c] 
    check = min(tmp) 
    
    if check not in stk and check // 1000 != 0 and check // 100 != 0 and check // 10 != 0:        
        stk.append(check)
    
for i in range(len(stk)):
    if stk[i] == ans:
        print(i + 1)
        print(stk[i])
        
