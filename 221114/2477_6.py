import sys
melon = int(sys.stdin.readline().rstrip())
dir = []
how = []
arr = []
for _ in range(6):
    direc, num = map(int, sys.stdin.readline().rstrip().split())
    dir.append(direc)
    how.append(num)
    arr.append([direc, num])

# 똑같은 수 연속인 경우, (dir) 그럼 직사각형
# 다른 수 연속이면 
# 3, 4나 1, 2에서 두번나오는 거의 첫번째꺼 