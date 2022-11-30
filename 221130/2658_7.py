# 일단 꼭짓점이 2개 1개 여야함 
# 2개 1개 일 때를 이제 고려해서
# 1개인 놈 기준으로 줄세우기 [0, 0, 0, 1 , 2, ,3, 2, ,1, 0 , 0]
# 1. 대칭 확인
# 2. 직각이려면 두개인 애한테 내렸을 때 딱 중앙이어야 함

import sys
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(10)]
total1 = []
total2 = []
vh1 = []
vh2 = []
out = []
for i in range(10):
    cnt1 = 0
    for j in range(10):
        if arr[i][j] == 1:
            cnt1 += 1
            ans_i = i
            ans_j = j
    if cnt1 == 1 and [ans_i + 1, ans_j + 1] not in vh1:
        vh1.append([ans_i + 1, ans_j + 1])
        total1.append(cnt1)
    else:
        total1.append(cnt1)

for i in range(10):
    cnt2 = 0
    for j in range(10):
        if arr[j][i] == 1:
            cnt2 += 1
            ans_i = i
            ans_j = j
    if cnt2 == 1 and [ans_j + 1, ans_i + 1] not in vh2:
        vh2.append([ans_j + 1, ans_i + 1])
        total2.append(cnt2)
    else:
        total2.append(cnt2)



# 1. 대칭 확인
vh = []
total = []
same = []
new = []
if len(vh1) == 2 and len(vh2) == 1:
    vh1 = vh1
    vh2 = vh2
    for i in range(len(total1)):
        if total1[i] != 0:
            total.append(total1[i])

elif len(vh1) == 1 and len(vh2) == 2:
    vh1, vh2 = vh2, vh1
    for i in range(len(total2)):
        if total2[i] != 0:
            total.append(total2[i])

else:
    for i in range(len(total1)):
        if total1[i] != 0:
            total.append(total1[i])
        if total2[i] != 0:
            same.append(total2[i])
    total.sort()
    same.sort()
    
    if total == same and len(total) > 0:
        # 6, 4
        if arr[vh2[0][0] - 1][vh1[0][1] - 1] == 1:
            new.append([vh2[0][0], vh1[0][1]])
        # 9, 7
        elif arr[vh1[0][0] - 1][vh2[0][1] - 1] == 1:
            new.append([vh1[0][0], vh2[0][1]])
        # 6, 4
        elif arr[vh2[0][0] - 1][vh1[0][1] - 1] == 1:
            new.append([vh2[0][0], vh1[0][1]])
        # 3, 7
        elif arr[vh1[0][0] - 1][vh2[0][1] - 1] == 1:
            new.append([vh1[0][0], vh2[0][1]])
        else:
            out.append('x')

    else:
        out.append('삼각형아님')

result = []
if len(out) == 0 and len(new) == 0:

    mid = len(total) // 2
    cnt_dec = 0
    for k in range(mid):
        if total[mid + k] == total[mid - k]:
            cnt_dec += 1
        else:
            out.append('0')
    if cnt_dec % 2 == 1:
        # 2. 직각 확인
        # vh1이 길이가 2,  vh2가 길이가 1
        if vh1[0][0] == vh1[1][0]:
            yy = (vh1[0][1] + vh1[1][1]) // 2
            if yy == vh2[0][1] :
                yy = vh2[0][1]
            else:
                out.append('1')
        elif vh1[0][1] == vh1[1][1]:
            xx = (vh1[0][0] + vh1[1][0]) // 2
            if xx == vh2[0][0] :
                xx = vh2[0][0]
            else:
                out.append('2')

        result.append(vh1[0])
        if vh1[1] not in result:
            result.append(vh1[1])
        if vh2[0] not in result:
            result.append(vh2[0])
        result.sort()
        
        
        
    else:
        out.append('대칭아님')
elif len(new) == 1:
    result.append(vh1[0])
    if vh2[0] not in result:
        result.append(vh2[0])
    if new[0] not in result:
        result.append(new[0])
    result.sort()
    


else:
    out.append('이미 오류')




if len(out) == 0 and len(result) == 3:
    for i in range(3):
        print(*result[i])    
        
else:
    print('0')


