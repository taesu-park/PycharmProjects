import sys
sys.stdin = open('input_Magnetic.txt','r')

for t in range(1, 11):
    A = int(input())

    count = 0
    arr = [list(map(int,input().split())) for _ in range(100)]
    for i in range(len(arr)):
        tmp = 0
        for j in range(len(arr[0])):
            if arr[j][i] == 1:
                tmp = 1
            elif arr[j][i] == 2 and tmp == 1:
                count += 1
                tmp = 0

    print('#{} {}'.format(t, count))