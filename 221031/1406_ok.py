import sys

stk = []
letter = list(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline())
for _ in range(N):
    order = list(sys.stdin.readline())

    if order[0] == 'L':
        if len(letter) > 0 :
            stk.append(letter.pop())
    elif order[0] == 'D':
        if len(stk) > 0:
            letter.append(stk.pop())
    elif order[0] == 'B':
        if len(letter) > 0:
            letter.pop()
    else:
        letter.append(order[2])

result = letter + stk[::-1]
for i in result:
    print(i, end="")