tc = int(input())
for i in range(tc):
    arr = list(input())
    arr2 = []
    cnt = 0
    # print(len(arr2))
    for j in range(len(arr)):
        if arr[j] == ' ':
            if len(arr2) == 0:
                for k in range(j):
                    arr2.append(j)
                    cnt += 1
                    print(arr[j - 1 - k], end="")

            else:
                for k in range(j - arr2[-1]):
                    arr2.append(j)
                    cnt += 1
                    print(arr[j - k], end="")
        elif j == len(arr) - 1:
            print(' ', end="")
            if len(arr2) != 0:
                for k in range(j - arr2[-1]):
                    print(arr[j - k], end="")
        else:
            if cnt == 0:
                for k in range(len(arr), 0, -1):
                    print(arr[k - 1], end="")
                break

                    
