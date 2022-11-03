import sys
line = sys.stdin.readline().rstrip()
stk = []
laser = 0
for i in range(len(line)):
    if line[i] == '(':
        if line[i + 1] == ')':
            stk.append(1)
        else:
            stk.append('(')
    else:
        if line[i - 1] == '(':
            pass
        else:
            stk.append(')')
laser = 0
stick = []
result = 0
print(stk)
for i in range(len(stk)):
    if stk[i] == 1:
        if stick:
            laser += 1
        else:
            laser = 0
    elif stk[i] == '(':
        stick.append(stk[i])
            
    else:
        stick.pop()
        if len(stick) == 0:
            print(f'1 {laser}')
            result += laser
            result += 1
            laser = 0
        else:
            print(f'2 {laser} {stick}')
            result += laser
            result += 1
print(result)