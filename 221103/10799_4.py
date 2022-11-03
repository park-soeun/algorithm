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
result = 0
laser = 0
print(stk)
for i in range(len(stk)):
    if stk[i] == '(':
        stick = ['(']
        for j in range(i + 1, len(stk)):
            if len(stick) != 0:
                if stk[j] == '(':
                    stick.append(stk[j])
                elif stk[j] == 1:
                    laser += 1
                else:
                    stick.pop()
                    result += laser
            else:
                print('error')

print(result)