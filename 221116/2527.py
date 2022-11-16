import sys
for _ in range(4):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    small = arr[0:4]
    large = arr[4:]

    small_x1 = small[0]
    small_x2 = small[2]
    small_y1 = small[1]
    small_y2 = small[3]
    small_height = small_y2 - small_y1
    small_width = small_x2 - small_x1

    small_rec = [[small_x1, small_y1], [small_x1, small_y2], [small_x2, small_y1], [small_x2, small_y2]]

    large_x1 = large[0]
    large_x2 = large[2]
    large_y1 = large[1]
    large_y2 = large[3]
    large_height = large_y2 - large_y1
    large_width = large_x2 - large_x1

    large_rec = [[large_x1, large_y1], [large_x1, large_y2], [large_x2, large_y1], [large_x2, large_y2]]
    # print(large_x_list)
    # cnt_point = 0
    # for i in small_rec:
    #     for j in large_rec:
    #         if i == j:
    #             same_x = i[0]
    #             same_y = i[1]

    # x2, x1 사이에 x1이나 x2가 사이에 있는지 확인
    # x1이나 x2에 딱 걸리면 선분이거나 점 겹칠수도... 아래 꼭지점이 동일한 경우 ! 
    # 
    # x1 < large_x1 < x2 인 경우 
    # 그 때 y1이나 y2가 걸리는 지 확인 
    # y1 < large_y1 < y2
    # x1 == large_x1 or x2 == large_x1 인경우 
    result = ''
    if small_x1 < large_x1 and large_x1 < small_x2:
        if large_y2 - small_y1 < large_height + small_height:
            result = 'a'
        elif large_y2 - small_y1 == large_height + small_height:
            result = 'b'
        else:
            result = 'd'
    elif small_x2 == large_x1 or small_x1 == large_x2:
        if large_y2 - small_y1 < large_height + small_height:
            result = 'b'
        elif large_y2 - small_y1 == large_height + small_height:
            result = 'c'
        else:
            result = 'd'
    elif large_x2 < small_x1 and small_x2 < large_x2:
        if large_y2 - small_y1 < large_height + small_height:
            result = 'a'
        elif large_y2 - small_y1 == large_height + small_height:
            result = 'b'
        else:
            result = 'd'

    else:
        result = 'd'
    print(result)
        



    

