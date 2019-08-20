import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    row_sum = col_sum = 0
    for i in range(N):
        row_sum = col_sum = 0
        for j in range(N):
            row_sum += arr[i][j]
            col_sum += arr[j][i]

