import sys
num = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(num)]
# a, f // 0 5
# b, d // 1 3
# c, e // 2 4 
# b c d e // 1 2 3 4 
# a c e f // 0 2 4 5
# a b d f // 0 1 3 5
candi = []
for i in range(num):
    # ceil_floor = [[0, 5], [1, 3], [2, 4], [1, 3], [2, 4], [0, 5]]
    # side = [[1, 2, 3, 4], [0, 2, 4, 5], [0, 1, 3, 5], [0, 2, 4, 5], [0, 1, 3, 5], [1, 2, 3, 4]]
    ceil_floor = [[0, 5], [1, 3], [2, 4]]
    side = [[1, 2, 3, 4], [0, 2, 4, 5], [0, 1, 3, 5]]
    j_arr = []
    candi2 = []

    for j in range(6):
        if arr[i][j] == 6:
            if j == 0 or j == 5:
                candi.append([[arr[i][2], arr[i][4]], [arr[i][1], arr[i][3]]])
                
            elif j == 1 or j == 3:
                candi.append([[arr[i][2], arr[i][4]], [arr[i][0], arr[i][5]]])
            else:
                candi.append([[arr[i][0], arr[i][5]], [arr[i][1], arr[i][3]]])
        # if arr[i][j] == 5:
        #     if j == 0 or j == 5:
        #         candi.append([arr[i][2], arr[i][4]])
        #         candi.append([arr[i][1], arr[i][3]])
        #     elif j == 1 or j == 3:
        #         candi.append([arr[i][2], arr[i][4]])
        #         candi.append([arr[i][0], arr[i][5]])
        #     else:
        #         candi.append([arr[i][0], arr[i][5]])
        #         candi.append([arr[i][1], arr[i][3]])
    
print(f'candi1 : {candi}')
# print(f'candi2 : {candi2}')
print()

    # floor_list = []
    # ceil_list = []
    # result = []
    # for j in range(2):
    #     for k in range(2):
    #         floor_list.append(candi[j][k])
    #         ceil_list.append(candi[j][abs(k - 1)])
    #         result.append(candi[j][abs(k - 1)])
    #         if result[-1] == candi[j][k]:
    #             result.append(candi[j][abs(k - 1)])
    #         else:
    #             print("이거 5")

    #         # if floor_list(-1) == candi[j][k]:

    # print(result)


    






