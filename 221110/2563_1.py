import sys
num = int(sys.stdin.readline().rstrip())
arr = []
# x = []
# y = []
for _ in range(num):
    ele = list(map(int, sys.stdin.readline().rstrip().split()))
    ele2 = []
    ele2.append(ele[0])
    ele2.append(ele[0] + 10)
    # x.append(ele[0])
    # x.append(ele[0] + 10)
    ele2.append(ele[1])
    ele2.append(ele[1] + 10)
    # y.append(ele[1])
    # y.append(ele[1] + 10)
    arr.append(ele2)
# print(x)