import sys
arr = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(4)] 
result = 0
# x좌표마다의 가장 높은 점과 가장 낮은 점 체크하기
# 걍 1로 채우기
paper = [[0] * 100 for _ in range(100)]
for i in range(4):
    for p in range(arr[i][0], arr[i][2]):
        for q in range(arr[i][1], arr[i][3]):
            if paper[p][q] == 0:
                paper[p][q] = 1
                result += 1
        
print(result)