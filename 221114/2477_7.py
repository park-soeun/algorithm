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
            paper[dot[i][0] - j][dot[i][1]] = 3

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

print(minX, minY, maxX, maxY)

            
        

# cnt2 = 0
# for i in range(minX, maxX + 1):
#     for j in range(minY, maxY + 1):
#         print(paper[i][j], end="")
#         if paper[i][j] != 0:
#             cnt2 += 1
   
       
#     print()

# print(cnt2)
width = []
for i in range(minY, maxY + 1):
    cnt_1 = 0
    for j in range(minX, maxX + 1):
        if paper[j][i] == 1:
            cnt_1 += 1
            if cnt_1 > 10:
                # print(cnt_1)
                # break
                width.append(i)
print(width)
print(len(width))
