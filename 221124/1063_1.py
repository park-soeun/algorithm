import sys
arr = [['R', [0, 1]], ['L', [0, -1]], ['T', [-1, 0]], ['B', [1, 0]], ['RT', [-1, 1]], ['LT', [-1, -1]], ['RB', [1, 1]], ['LB', [1, -1]]]

loca_r, loca_k, num = sys.stdin.readline().rstrip().split()
num = int(num)
move = [sys.stdin.readline().rstrip() for _ in range(num)]
# a2는 6, 0 
# b2는 6, 1
# c2는 6, 2
# print(ord('A') - 65)
# print(ord('B') - 65)
# print(ord('C') - 65)
# print(ord('D') - 65)
# print(loca_r[:1])
# print(loca_r[1:])
loca1 = [(int(loca_r[1:]) - 8) * (-1), ord(loca_r[:1]) - 65]
loca2 = [(int(loca_k[1:]) - 8) * (-1), ord(loca_k[:1]) - 65]
print('원본')
print(loca1, loca2)

for i in range(num):
    for j in range(len(arr)):
        if move[i] == arr[j][0]:
            # move[i] = arr[j][1]
            if 0 <= loca1[0] + arr[j][1][0] < 8 and 0 <= loca1[1] + arr[j][1][1] < 8:
                loca1[0] += arr[j][1][0]
                loca1[1] += arr[j][1][1]
                if loca1 == loca2 and 0 <= loca2[0] + arr[j][1][0] < 8 and 0 <= loca2[1] + arr[j][1][1] < 8:
                    loca2[0] += arr[j][1][0]
                    loca2[1] += arr[j][1][1]
                elif loca1 != loca2:
                    continue
                else:
                    loca1[0] -= arr[j][1][0]
                    loca1[1] -= arr[j][1][1]
print('바뀐거') 
print(loca1, loca2)
loca1 = [chr(loca1[1] + 65), (loca1[0] - 8) * (-1)]
loca2 = [chr(loca2[1] + 65), (loca2[0] - 8) * (-1)]
print(f'{loca1[0]}{loca1[1]}')
print(f'{loca2[0]}{loca2[1]}')

