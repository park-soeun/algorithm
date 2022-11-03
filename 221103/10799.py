import sys
line = sys.stdin.readline().rstrip()
stk = []
laser = 0
stick = 0
result = 0
for i in range(len(line)):
    if line[i] == '(':
        stk.append(line[i])
        stick += 1
    elif line[i] == ')':
        if line[i - 1] == '(':
            stk.pop()
            # stk.append('x')
            stick -= 1
            laser += 1
        else:
            if stick != 0:
                stk.append(')')
                stick -= 1
                result += laser
                result += 1
            else:
                laser = 0
                stick = 0
print(laser)
print(stk)
print(result)