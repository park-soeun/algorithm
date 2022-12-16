import sys
num = list(map(int, sys.stdin.readline().rstrip().split()))
stk = [1111]
sorted_num = sorted(num)
ans = sorted_num[0] * 1000 + sorted_num[1] * 100 + sorted_num[2] * 10 + sorted_num[3]
tmp = 0
tmp1 = []
for thou in range(1, 10):
    for hund in range(1, 10):
        for ten in range(1 ,10):
            for one in range(1, 10):
                tmp1 = [thou, hund, ten, one]
                tmp2 = sorted(tmp1)
                tmp = tmp2[0] * 1000 + tmp2[1] * 100 + tmp2[2] * 10 + tmp2[3]
                if stk[-1] != ans:
                    if tmp not in stk:
                        stk.append(tmp)
print(len(stk))
print(stk)