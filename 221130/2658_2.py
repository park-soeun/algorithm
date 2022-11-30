import sys
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(10)]
vert = []
hori = []
for i in range(10):
    cnt1 = 0
    for j in range(10):
        if arr[i][j] == 1:
            cnt1 += 1
            ans_i = i
            ans_j = j
    if cnt1 == 1:
        vert.append([ans_i + 1, ans_j + 1])
    
        
cnt2 = 0
for i in range(10):
    for j in range(10):
        if arr[j][i] == 1:
            cnt2 += 1
            ans_i = i
            ans_j = j
    if cnt2 == 1:
        hori.append([ans_j + 1, ans_i + 1])
    else:
        cnt2 = 0
if len(vert) == 2 and len(hori) == 1:
    p1_b = (vert[0][1] - hori[0][1])
    p2_b = (vert[1][1] - hori[0][1])
    p1_a = (vert[0][0] - hori[0][0])
    p2_a = (vert[1][0] - hori[0][0])
    # incli1 = (vert[0][1] - hori[0][1]) / (vert[0][0] - hori[0][0])
    # incli2 = (vert[1][1] - hori[0][1]) / (vert[1][0] - hori[0][0])
    incli1 = p1_b / p1_a
    incli2 = p2_b / p2_a

    multi_incli = incli1 * incli2
    len1 = (p1_b) * (p1_b) + (p1_a) * (p1_a)
    len2 = (p2_b) * (p2_b) + (p2_a) * (p2_a)
    result = []
    vert.sort()
    result.append(vert[0])
    result.append(hori[0])
    result.append(vert[1])

    if len1 == len2 and multi_incli == -1:
        for i in range(len(result)):
            print(*result[i])
    else:
        print('0')
else:
    print('0')