import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr2 = [[0]*N for _ in range(N)]
    asum = 0
    row_sum = col_sum = 0
    for i in range(N):
        for j in range(N):
            row_sum = col_sum = 0
            for k in range(N):
                row_sum += arr[i][k]
                col_sum += arr[k][j]
            arr2[i][j] += row_sum + col_sum - arr[i][j]
    arrmax = 0
    row = col = 0
    for x in range(N):
        for y in range(N):
            if arrmax <= arr2[x][y]:
                arrmax = arr2[x][y]
                row = x
                col = y
    print(arrmax, row, col)
    # row_sum = col_sum = 0R
    # ans = 0
    # row = col = 0
    # arr2 = []
    # arr3 = []
    # for i in range(N):
    #     row_sum = col_sum = 0
    #     for j in range(N):
    #         row_sum += arr[i][j]
    #         col_sum += arr[j][i]
    #     arr2.append(row_sum)
    #     arr3.append(col_sum)
    # xmax = ymax = 0
    # for x in range(len(arr2)):
    #     if xmax <= arr2[x]:
    #         xmax = arr2[x]
    #         row = x
    # for y in range(len(arr3)):
    #     if ymax <= arr3[y]:
    #         ymax = arr3[y]
    #         col = y
    #
    # ans = xmax + ymax - arr[row][col]
    # print(ans, row, col)

