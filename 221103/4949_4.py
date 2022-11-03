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
                print('no')
                break
        elif line[i] == '[':
            stk.append('[')
        elif line[i] == ']':
            if len(stk) != 0:
                if stk[-1] == '[':
                    stk.pop()
                else:
                    stk.append(']')
            else:
                print('no')
                break
        elif line[i] == '.':
            if len(stk) == 0:

                print('yes')
            else:
                print('no')
        
