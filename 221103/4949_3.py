while True:
    line = input()
    if line == '.':
        break
    stk = []
    for i in range(len(line)):
        if line[i] == '(':
            stk.append('(')
        elif line[i] == ')':
            if len(stk) != 0:
                if stk[-1] == '(':
                    stk.pop()
                else:
                    stk.append(')')
            else:
                stk.append(')')

        elif line[i] == '[':
            stk.append('[')
        elif line[i] == ']':
            if len(stk) != 0:
                if stk[-1] == '[':
                    stk.pop()
                else:
                    stk.append(']')
            else:
                stk.append(']')
        if len(stk) == 0:
            print(stk)
            print('yes')
            break   
        else:
            print(stk)
            print('no')
            break

