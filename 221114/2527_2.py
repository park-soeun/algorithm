# 각 꼭지점에 그냥 1을 더해서 2가되면 뭐 2가 선분이거나.. 2가 한개거나 2가..음 사각형을 이룰 때?
# 꼭짓점이 내부에 있거나
# 꼭짓점이 내부에 있지 않아도 겹칠 수도 있음..
# 그러면 내부에 해당하면 걍 다 1로 ..?  ㅇㅋ

import sys
for _ in range(4):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    small = arr[0:4]
    large = arr[4:]
    rect = []
    rect.append(small)
    rect.append(large)
    max_length = max(arr)
    paper = [[0 for _ in range(max_length + 1)] for _ in range(max_length + 1) ]
    cnt1 = 0
    cnt2 = 0
    print(large, small)
    for i in range(small[0], small[2] + 1):
        for j in range(small[1], small[3] + 1):
            if paper[i][j] == 0:
                paper[i][j] = 1
    
    
    for i in range(large[0], large[2] + 1):
        for j in range(large[1], large[3] + 1):
            if paper[i][j] == 1:
                paper[i][j] = 2
    cnt = 0
    check = 0
    print(cnt1, cnt2)
    for i in range(max_length):
        if 2 in paper[i]:
            cnt += 1
    print(cnt)