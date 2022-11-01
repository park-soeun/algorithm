tc = int(input())
for i in range(tc):
    arr = list(input())
    arr2 = []
    cnt = 0
    for j in range(len(arr)):
        if arr[j] == ' ':
            arr2.append(j)
            cnt += 1
    arr2.append(len(arr))
    if cnt != 0:
        for k in range(arr2[0]):
            print(arr[arr2[0] - k - 1], end="")
        print(' ', end="")
        
        for k in range(len(arr2) - 1):
            tmp = arr[arr2[k]:arr2[k+1]:]
            tmp = tmp[::-1]
            for ele in tmp:
                print(ele, end="")

    else:
        for k in range(len(arr)):
            print(arr[len(arr) - k - 1],  end="")
    print()