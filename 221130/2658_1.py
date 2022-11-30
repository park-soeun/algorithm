import sys
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(10)]
vert = []
hori = []
total1 = []
total2 = []
out = []
rever = 0
for i in range(10):
    cnt1 = 0
    for j in range(10):
        if arr[i][j] == 1:
            cnt1 += 1
            ans_i = i
            ans_j = j
    if cnt1 == 1 and [ans_i + 1, ans_j + 1] not in vert:
        vert.append([ans_i + 1, ans_j + 1])
        total1.append(cnt1)
    else:
        total1.append(cnt1)

        
cnt2 = 0
for i in range(10):
    for j in range(10):
        if arr[j][i] == 1:
            cnt2 += 1
            ans_i = i
            ans_j = j
    print(cnt2)
    if cnt2 == 1 and [ans_j + 1, ans_i + 1] not in hori:
        hori.append([ans_j + 1, ans_i + 1])
        total2.append(cnt2)
        cnt2 = 0
    else:
        total2.append(cnt2)
        cnt2 = 0
print(total2)
print(vert, hori)
if len(vert) > len(hori):
    vert = vert
else:
    vert, hori = hori, vert
    rever = 1
print(vert, hori)
if len(vert) == 2 and len(hori) == 1:
    p1_b = (vert[0][1] - hori[0][1])
    p2_b = (vert[1][1] - hori[0][1])
    p1_a = (vert[0][0] - hori[0][0])
    p2_a = (vert[1][0] - hori[0][0])
    # incli1 = (vert[0][1] - hori[0][1]) / (vert[0][0] - hori[0][0])
    # incli2 = (vert[1][1] - hori[0][1]) / (vert[1][0] - hori[0][0])
    incli1 = p1_b / p1_a
    incli2 = p2_b / p2_a

    # 갯수 확인
    total3 = []
    max_point = 0
    total = []
    print(total1, total2)
    if rever == 0:
        total = total1
    else:
        total = total2
    print('여기')
    print(total)
    max_point1 = 0
    max_point2 = 0
    for p in range(len(total)):
        # if rever == 0:
        if max_point < total[p]:
            max_point = p + 1
        if total[p] != 0:
            total3.append(total[p])
    #     else:

    # print(total2)
    print(hori)
    print(total3)

    # if max_point == hori[0]:
    max_point = hori[0][0]
    print(max_point)
    xx = len(total3)//2
    for q in range(len(total3) // 2):
        left = total3[xx - q]
        right = total3[xx + q]
        if left == right:
            continue
        else:
            out.append('1')
# else:
#     out.append('2')

    # 기울기 확인
    multi_incli = incli1 * incli2
    len1 = (p1_b) * (p1_b) + (p1_a) * (p1_a)
    len2 = (p2_b) * (p2_b) + (p2_a) * (p2_a)
    result = []
    vert.sort()
    result.append(vert[0])
    result.append(hori[0])
    result.append(vert[1])
    result.sort()

    if len1 == len2 and multi_incli == -1 and len(out) == 0:
        for i in range(len(result)):
            print(*result[i])
    else:
        print('0')
else:
    print('0')