import sys
sys.stdin = open('../txt/input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 행 우선 순회
    # 모든 자료의 합
    total = 0
    row_sum = col_sum = 0
    ans = 100000000
    for i in range(N): # 0 ~ N - 1
        row_sum = col_sum = 0
        for j in range(N): # 0 ~ N - 1
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        if row_sum <= ans:
            ans = row_sum
        if col_sum <= ans:
            ans = col_sum
        # ans = min(ans, row_sum, col_sum)
    print(ans)
    # S = 0
    # for i in range(N): # 좌상단 --> 우하단
    #     S += arr[i][i]
    # ans = min(ans, S)
    # S = 0
    # for i in range(N):
    #     S += arr[i][N -1 -i]
    # ans = min(ans, S)