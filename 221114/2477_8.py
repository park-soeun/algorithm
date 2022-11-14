import sys
melon = int(sys.stdin.readline().rstrip())
arr = []
arr = [[500, 500]]
for i in range(6):
    dir, amount = map(int, sys.stdin.readline().rstrip().split())
    if dir == 1:
        arr.append([arr[i][0] + amount, arr[i][1]])
    elif dir == 2:
        arr.append([arr[i][0] - amount, arr[i][1]])
    elif dir == 3:
        arr.append([arr[i][0], arr[i][1] - amount])
    else:
        arr.append([arr[i][0], arr[i][1] + amount])

x_list = []
y_list = []
for i in range(len(arr)):
    if arr[i][0] not in x_list:
        x_list.append(arr[i][0])
    if arr[i][1] not in y_list:
        y_list.append(arr[i][1])
x_list.sort()
y_list.sort()

point = [[min(x_list), min(y_list)], [min(x_list), max(y_list)], [max(x_list), min(y_list)], [max(x_list), max(y_list)]]

print(point)
not_point = []
for ele in point:
    if ele not in arr:
        not_point = ele
print(not_point)
mid_point = [x_list[1], y_list[1]]
print(mid_point)
print(max(x_list))
big_rect = (max(x_list) - min(x_list)) * (max(y_list) - min(y_list))
print(big_rect)
sm_rec = abs((mid_point[0] - not_point[0]) * (mid_point[1] - not_point[1]))
print(sm_rec)
result = big_rect - sm_rec
print(result * melon)
