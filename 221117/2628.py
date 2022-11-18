import sys
width, height = map(int, sys.stdin.readline().rstrip().split())
num = int(sys.stdin.readline().rstrip())
x_cut = []
y_cut = []
for i in range(num):
    xy, point = map(int, sys.stdin.readline().rstrip().split())
    if xy == 0:
        x_cut.append(point)
    else:
        y_cut.append(point)

x_cut.sort(reverse=True)
y_cut.sort(reverse=True)
y_point = [width]
x_point = [height]

# print(x_cut)
for i in y_cut:
    y_point.append(y_point.pop() - i)
    y_point.append(i)

for i in x_cut:
    x_point.append(x_point.pop() - i)
    x_point.append(i)

print(max(x_point) * max(y_point))