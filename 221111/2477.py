import sys
melon = int(sys.stdin.readline().rstrip())
dot = [[500, 500]]
tmp = []
paper = [[0 for _ in range(1000)] for _ in range(1000) ]
for i in range(6):
    direc, how = map(int, sys.stdin.readline().rstrip().split())
    if direc == 1:
        dot.append([dot[i][0] + how, dot[i][1]])
        for j in range(how):
            paper[dot[i][0] + j][dot[i][1]] = 1

    elif direc == 2:
        dot.append([dot[i][0] - how, dot[i][1]])
        for j in range(how):
            paper[dot[i][0] - j][dot[i][1]] = 1

    elif direc == 3:
        dot.append([dot[i][0], dot[i][1] - how])
        for j in range(how):
            paper[dot[i][0]][dot[i][1] - j] = 1

    else:
        dot.append([dot[i][0], dot[i][1] + how])
        for j in range(how):
            paper[dot[i][0]][dot[i][1] + j] = 1

    tmp.append([direc, how])
minX = 500
minY = 500
maxX = 500
maxY = 500
cnt = 0
# print(cnt)

for i in range(len(dot)):
    if minX > dot[i][0]:
        minX = dot[i][0]
    if minY > dot[i][1]:
        minY = dot[i][1]
    if maxX < dot[i][0]:
        maxX = dot[i][0]
    if maxY < dot[i][1]:
        maxY = dot[i][1]
# for i in range(len(dot)):
#     dot[i][0] -= minX
#     dot[i][1] -= minY
# print(dot)
cnt2 = 0
for i in range(minX - 1, maxX + 2):
    for j in range(minY - 1, maxY + 2):
        print(paper[i][j], end="")
        if paper[i][j] == 1:
            cnt2 += 1
    print()
print(cnt2)
# 왼쪽끝이 1인 순간부터 오른쪽 끝이 1인 순간까지 1로 채우기
# 위아래왼쪽오른쪽이 다 1인 순간 1로 채우기 
# for i in range(minX - 3, maxX + 3):
#     for j in range(minY - 3, maxY + 3):
#         # if paper[minX][j] == 1:
#         #     paper[i][j] = 1
#         if paper[i][j] == 1:
#             # k = 1
#             # while paper[i + k][j] != 1:
#             #     paper[i + k][j] = 1
#                 # k += 1
#             for k in range(1, maxX):
#                 if paper[i + k][j] == 0:
#                     paper[i + k][j] = 1
#                 else:
#                     break
for i in range(minX - 3, max + 3):
    if[minX]


# for i in range(1000):
#     for j in range(1000):
#         if paper[i][j] == 1:
#             cnt += 1
# print(cnt)
print(cnt)
print(minX, minY, maxX, maxY)

for i in range(minX-1, maxX - 3):
    for j in range(minY-3, maxY + 2):
        print(paper[i][j], end="")
        if paper[i][j] == 1:
            cnt += 1
    print()

print(cnt)