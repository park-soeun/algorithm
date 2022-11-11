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
tmp = []
for i in range(num):
    to_zero = store[i][0] + store[i][1]
    to_finish = x + y - to_zero
    tmp = [to_zero, to_finish, store[i][2]]
    how = store[i][2] + dg[2]
    candid = []
    print(f'tmp: {tmp}')
    if how % 2 == 0:
        candid.append(abs(tmp[0] - dg[0]))
        candid.append(2 * x + 2 * y - candid[0])
    else:
        candid.append(tmp[0] + dg[0] + dg[1])
        print(f't:{tmp}')
        print(f'd:{dg}')
        candid.append(2 * x + 2 * y - candid[0])
    
    print(candid)
    print(min(candid))
    result += min(candid)
print(result)
    

    

    

