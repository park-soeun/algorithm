import sys
num = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
# stk = [0] * num
stk = [0] * num
for i in range(num):
    if arr[i] == 0:
        stk[i] = i
        print(stk)
    else:
        stkf = stk[0:i]
        stkb = stk[i:]
        stkb.append(i)
        print(stkf, stkb)
        stk.append(stkb[-1])
        print(stkb)

        
print(stk)
    
    
    
    

# 1
# 1 2
# 1 3 2 
# 1 3 2 4
# 1 3 5 2 4

# 1. slice 해서 사이에 끼워넣기
# 2. 0,0,0,0,0 배열 만든 다음에 중간 중간 땡기기??

# i 일 때 뒤에 0을 추가하고 하나 미뤄 ?
