import sys
sys.stdin = open('input_LED.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    M = list(map(int,input().split()))
    arr = [0] * N
    count = 0

    for j in range(1, len(M)+1):
        if j == 1:
            if arr[j-1] == M[j - 1]:
                continue
            else:
                for i in range(1, len(M)+1):
                    if arr[i-1] == 0:
                        arr[i-1] = 1
                    elif arr[i-1] == 1:
                        arr[i-1] = 0
                count += 1
        else:
            if arr[j - 1] == M[j - 1]:
                continue
            else:

                for k in range(j, len(M)+1, j):

                    if arr[k - 1] == 0:
                        arr[k - 1] = 1
                    elif arr[k - 1] == 1:
                        arr[k - 1] = 0
                count += 1
        print(arr,M)
        if arr == M:
            break

    print(count)
