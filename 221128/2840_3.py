import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
result = ['?'] * N
arr = [list(sys.stdin.readline().rstrip().split()) for _ in range(K)] 
# print(arr)
idx = 0

for i in range(K):
    idx += int(arr[i][0])
    txt = arr[i][1]

    how = idx // N
    if how == 0:
        if result[idx] == '?' or result[idx] == txt:
            result[idx] = txt
        else:
            result = ["!"]
            break
    else:
        idx -= how * N
        if result[idx] == '?' or result[idx] == txt:
            result[idx] = txt
        else:
            result = ["!"]
            break

last_letter = arr[-1][1]
cutting_idx = 0
for i in range(N):
    if result != ["!"]:
        if result[i] == last_letter and len(result) > 1:
            cutting_idx = i
            first = result[cutting_idx::-1]
            end = result[:cutting_idx:-1]

            result = first + end
            break
    
for i in range(len(result)):
    for j in range(i + 1, len(result)):
        if result[i] == result[j]:
            if result[i] != "?":
                # print(i)
                result = ["!"]
                break
                # pass
    


for i in range(len(result)):
    print(result[i], end="")
