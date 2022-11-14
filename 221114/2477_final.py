import sys
melon = int(sys.stdin.readline().rstrip())
dot = [[500, 500]]
tmp = []
paper = [[0 for _ in range(1000)] for _ in range(1000)]
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

for i in range(len(dot)):
    if minX > dot[i][0]:
        minX = dot[i][0]
    if minY > dot[i][1]:
        minY = dot[i][1]
    if maxX < dot[i][0]:
        maxX = dot[i][0]
    if maxY < dot[i][1]:
        maxY = dot[i][1]
for i in range(len(dot)):
    dot[i][0] -= minX
    dot[i][1] -= minY

x_list = []
y_list = []
finalX = 0
finalY = 0
for i in range(len(dot)):
    if dot[i][0] not in x_list:
        x_list.append(dot[i][0])
    if dot[i][1] not in y_list:
        y_list.append(dot[i][1])


x_list.sort()
y_list.sort()
result = 0

rect = [[0, 0], [max(x_list), 0], [0, max(y_list)], [max(x_list), max(y_list)]]


no_point = []
for point in rect:
    if point not in dot:
        no_point = point
if len(x_list) > 2 and len(y_list) > 2 and len(no_point) > 0:
    result = (max(x_list) * max(y_list)) - ((abs(x_list[1] - no_point[0])) * abs((y_list[1] - no_point[1]) ))
else:
    result = (max(x_list) * max(y_list))


print(result * melon)