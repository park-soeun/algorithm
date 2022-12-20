def solution(s):
    answer = []
    cnt = 0
    cnt0 = 0
    while s != '1':
        cnt1 = 0
        cnt += 1
        for i in range(len(s)):
            if s[i] == '1':
                cnt1 += 1
            else:
                cnt0 += 1
        tmp = []
        while cnt1 != 1:
            tmp.append(str(cnt1 % 2))
            cnt1 //= 2
        else:
            tmp.append('1')
        tmp.reverse()
        result = ''.join(tmp)
        s = result
    
    answer.append(cnt)
    answer.append(cnt0)
    return answer

solution('01110')