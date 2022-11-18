import sys
num = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(num)]
candi = []
candi2 = []
for i in range(num):
    ceil_floor = [[0, 5], [1, 3], [2, 4]]
    side = [[1, 2, 3, 4], [0, 2, 4, 5], [0, 1, 3, 5]]
    j_arr = []

    for j in range(6):
        if arr[i][j] == 6:
            if j == 0 or j == 5:
                candi.append([[arr[i][2], arr[i][4]], [arr[i][1], arr[i][3]]])
                
            elif j == 1 or j == 3:
                candi.append([[arr[i][2], arr[i][4]], [arr[i][0], arr[i][5]]])
            else:
                candi.append([[arr[i][0], arr[i][5]], [arr[i][1], arr[i][3]]])
        if arr[i][j] == 5:
            if j == 0 or j == 5:
                candi2.append([[arr[i][2], arr[i][4]], [arr[i][1], arr[i][3]]])
            elif j == 1 or j == 3:
                candi2.append([[arr[i][2], arr[i][4]], [arr[i][0], arr[i][5]]])
            else:
                candi2.append([[arr[i][0], arr[i][5]], [arr[i][1], arr[i][3]]])
    


first = candi.pop(0)
trash = candi2.pop(0)
total_list = []
for p in range(2):
    for q in range(2):
        cnt = 1
        total = 6
        result = []
        result.append(first[p][q])
        for i in range(len(candi)):
            for j in range(2):
                for k in range(2):
                    if result[-1] == candi[i][j][k]:
                        result.append(candi[i][j][abs(k - 1)])
                        total += 6
                        cnt += 1 
                        break
                    elif result[-1] == candi2[i][j][k]:
                        result.append(candi2[i][j][abs(k - 1)])
                        total += 5
                        cnt += 1
                        break
        total_list.append(total + (num - cnt) * 4)            
print(max(total_list))