import sys
w, h = map(int, sys.stdin.readline().rstrip().split())
p, q = map(int, sys.stdin.readline().rstrip().split())
t = int(sys.stdin.readline().rstrip())
paper = [[0] * (w + 1) for _ in range(h + 1)]
# paper[3][1] = 1
# paper[4][2] = 2
# paper[3][3] = 3
# paper[q][p] = 1
# paper[q + 1][p + 1] = 2

# dir = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
# dir = [[1, -1], [-1, -1] [1, -1], [-1, -1]]
# dir = 0 일 때는 y = 4인 경우 > dir = 3 > x = 6 인경우 > dir = 2
# dir = 1 일 때는 

# print(h - q, p)
dir = [1, 1]
nj = q
ni = p
paper[nj][ni] = 1
for i in range(1, t + 1):
    nj = nj + dir[0]
    ni = ni + dir[1]
    paper[nj][ni] = 1
    for i in range(h + 1):
        print(paper[i])
    print(nj, ni)
    print(dir)
    if nj == 0 or nj == h:
        dir[0] = -(dir[0])
        print("지금")
    if ni == 0 or ni == w:
        dir[1] = -(dir[1])
        print("아니 지금")
        print(dir)
print(nj, ni)


