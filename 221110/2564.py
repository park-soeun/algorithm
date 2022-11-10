import sys
x, y = map(int, sys.stdin.readline().rstrip().split())
arr = [[0 for _ in range(x)] for _ in range(y)]
num = int(sys.stdin.readline().rstrip())
store = []
for _ in range(num + 1):
    loca, dist = map(int, sys.stdin.readline().rstrip().split())
    if loca == 1:
        store.append([dist, y])
    elif loca == 2:
        store.append([dist, 0])
    elif loca == 3:
        store.append([0, y - dist])
    else:
        store.append([x, y - dist])

dg = store.pop()
# print(store)
# print(dg)
result = 0
for i in range(num):
    if store[i][1] != dg[1]:
        x_1 = 2 * x - store[i][0] - dg[0]
        x_2 = dg[0] + store[i][0]

        y_1 = 2 * y - store[i][1] - dg[1]
        y_2 = dg[1] + store[i][1]

        final_x = min(x_1, x_2)
        final_y = min(y_1, y_2)

    else:
        final_x = store[i][0] - dg[0]
        final_y = 0



    result += final_x + final_y
print(result)