# 작고 작으면 직사각형 > 근데 아예 겹치는 모양은 어떻게..?
# 꼭지점 하나가 겹치면 점
# 꼭지점 하나가 겹치고 거기다가 뭐 레벨이 같은 경우

import sys
for _ in range(4):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    small = arr[0:4]
    large = arr[4:]
    