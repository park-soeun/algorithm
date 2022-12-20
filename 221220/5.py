def solution(s):
    answer = []
    result = s
    cnt = 0
    cnt0 = 0
    while result != '1':
        cnt += 1
        tmp1 = ''
        cnt1 = 0
        for i in range(len(result)):
            if result[i] == 1:
                cnt1 += 1
        print(cnt1)
        result = 1
        # stk = ''
        # while tmp != 1:
        #     stk += (str(tmp % 2))
        #     tmp = tmp // 2
        # else:
        #     stk += '1'        
        # result = stk

        

    return answer
solution('01110')