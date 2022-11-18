import sys
num = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(num)]
floor_ceil = [[0, 5], [1, 3], [2, 4]]
paper = []
for i in range(num):
    point = []
    for p in range(len(floor_ceil)):
        # print(arr[i][floor_ceil[0][1]])
        point.append([arr[i][floor_ceil[p][0]], arr[i][floor_ceil[p][1]]])
    paper.append(point)
first = paper.pop(0)
result_list = []
# print()
for i in range(3):
    for j in range(-1, 2, 2):
        result = first[i][::j]
        # print(result)
        for p in range(len(paper)):
            for q in range(3):
                for r in range(2):
                    if result[-1] == paper[p][q][r]:
                        result.append(paper[p][q][abs(r - 1)])
                        break
        cnt6 = 0
        # print(result)
        for j in range(len(result)):
            if result[j] == 6:
                cnt6 += 1
        result_list.append(num * 6 - cnt6 * 1)
        # print(result_list)

print(max(result_list))

