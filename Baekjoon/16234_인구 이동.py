N, L, R = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] -