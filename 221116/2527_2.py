import sys
for _ in range(4):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    small = arr[0:4]
    large = arr[4:]
    # x_list, y_list저장해서걔네 카운트 ?

    small_x1 = small[0]
    small_x2 = small[2]
    small_y1 = small[1]
    small_y2 = small[3]
    small_height = small_y2 - small_y1
    small_width = small_x2 - small_x1
    small_x_list = [i for i in range(small_x1, small_x2 + 1)]
    small_y_list = [i for i in range(small_y1, small_y2 + 1)]


    large_x1 = large[0]
    large_x2 = large[2]
    large_y1 = large[1]
    large_y2 = large[3]
    large_height = large_y2 - large_y1
    large_width = large_x2 - large_x1

    cnt_x = 0
    cnt_y = 0

    for i in range(len(small_x_list)):
        if large_x1 - 1 < small_x_list[i] and small_x_list[i] < large_x2 + 1:
            cnt_x += 1
    
    for i in range(len(small_y_list)):
        if large_y1 - 1 < small_y_list[i] and small_y_list[i] < large_y2 + 1:
            cnt_y += 1
    
    result = 'd'
    if cnt_x == 1:
        if cnt_y == 1:
            result = 'c'
        elif cnt_y > 1:
            result = 'b'
    elif cnt_x > 1:
        if cnt_y == 1:
            result = 'b'
        elif cnt_y > 1:
            result = 'a'
    print(result)
        
        
