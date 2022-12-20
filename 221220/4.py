def solution(s):
    answer = []
    cnt1 = 0
    cnt2 = 0
    while s != '1':
        cnt2 += 1
        tmp1 = []
        for i in range(len(s)):
            if s[i] == '0':
                cnt1 += 1
            else:
                tmp1.append(s[i])
        tmp2 = len(tmp1) 
        tmp3 = ''
        print(tmp2)
        while tmp2 != 1 and tmp3 != 0:
            tmp3 += str(tmp2 % 2)
            tmp2 = tmp2 // 2
        
        s = tmp3
        print(s)
    
    print(cnt1, cnt2)
    return answer
solution('01110')