import sys

def count(data):
    maxV = 1
    for i in range(num):
        cnt1 = 1
        cnt2 = 1
        for j in range(1, num):
            if data[i][j] == data[i][j - 1]:
                cnt1 += 1
            else:
                cnt1 = 1
            if data[j][i] == data[j - 1][i]:
                cnt2 += 1
            else:
                cnt2 = 1
                
            maxV = max(maxV, cnt1, cnt2)
        
    return maxV

num = int(sys.stdin.readline().rstrip())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(num)]
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

ans = 0
            
        
            

for i in range(num):
    for j in range(num):
        tmp = [item[:] for item in arr]
        if j + 1 < num:
            tmp[i][j] = arr[i][j + 1]
            tmp[i][j + 1] = arr[i][j]
            candi = count(tmp)
            ans = max(ans, candi)
        if i + 1 < num:
            tmp[i][j] = arr[i + 1][j]
            tmp[i + 1][j] = arr[i][j]
            candi = count(tmp)
            ans = max(ans, candi)
            
            
  
print(ans)