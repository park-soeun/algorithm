import sys
x, y = map(int, sys.stdin.readline().rstrip().split())
arr = [[0 for _ in range(x)] for _ in range(y)]
num = int(sys.stdin.readline().rstrip())
store = []
for _ in range(num + 1):
    loca, dist = map(int, sys.stdin.readline().rstrip().split())
    if loca == 1:
        store.append([dist, y, loca])
    elif loca == 2:
        store.append([dist, 0, loca])
    elif loca == 3:
        store.append([0, y - dist, loca])
    else:
        store.append([x, y - dist, loca])

dg = store.pop()
result = 0
cnt_clock = 0
cnt_counter = 0
print(store)
print(dg)
dg_clock = dg[0] + dg[1]
dg_counter = y + x - dg[0] - dg[1]
dg_len = [dg_clock, dg_counter]
store_len = []
for i in range(num):
    cnt_zero = store[i][0] + store[i][1]
    cnt_finish = x + y - cnt_zero
    if store[i][2] % 2 != 0:
        to_zero = cnt_zero + dg_len[0]
        to_finish = 
    else:
        to_zero = cnt_zero - dg_len[0]
    store_len = [cnt_zero, cnt_finish]
    print(i + 1, store_len)

print(dg_len)