import sys
x, y = map(int, sys.stdin.readline().rstrip().split())
arr = [[0 for _ in range(x)] for _ in range(y)]
num = int(sys.stdin.readline().rstrip())
store = []
for _ in range(num + 1):
    loca, dist = map(int, sys.stdin.readline().rstrip().split())
    store.append([loca, dist])
dg = store.pop()

for i in range(num):
    if store[i][0] == dg[0] or store[i][1] == dg[1]:
        leng = abs(dg[1] - store[i][1]) + abs(store[i][0] -dg[0])
    else:
        






print(store)
print(dg)