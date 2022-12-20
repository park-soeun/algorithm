def solution(s):
    tmp1 = []
    answer = []
    for i in range(len(s)):
        if s[i] == '1':
            tmp1.append(s[i])
    
    tmp2 = len(tmp1)
    while tmp2 != 1:
        answer += tmp2 % 2
        tmp2 = tmp2 // 2
            
    return answer
solution('01110')