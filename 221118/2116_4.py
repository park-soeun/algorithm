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
# print(first)
print(candi)
print(candi2)
for p in range(2):
    for q in range(2):
        total = 6
        result = []
        result.append(first[p][q])
        cnt = 1
        cnt2 = 0
        # print(f'num = {num}')
        # while len(result) < 2:
        for i in range(len(candi)):
            for j in range(2):
                for k in range(2):
                    # print(result)
                    if len(result) < num and result[-1] == candi[i][j][k]:
                        result.append(candi[i][j][abs(k - 1)])
                        total += 6
                        cnt += 1 
                        # print('1이거')
                        break
                    elif len(result) < num and result[-1] == candi2[i][j][k]:
                        result.append(candi2[i][j][abs(k - 1)])
                        # print(i, j, k, result[-1])
                        total += 5
                        cnt2 += 1
                        # print('2이거')
                        break
                    
        # print(cnt, cnt2)
        if cnt2 % 2 == 0:
            cnt += 1
            cnt2 -= 1
        print(cnt, cnt2)
        total_list.append(cnt * 6 + cnt2 * 5)
        # total_list.append(total + cnt2 * 5 + (num - cnt - cnt2) * 4)        
        print(result)
        print(total_list)
        # for x in range(0, num - 1):
        #     if result[x] == 6:
        # print(total_list)    
print(max(total_list))