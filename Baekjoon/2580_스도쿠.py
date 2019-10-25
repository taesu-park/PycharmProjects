def BFS(x, y):
    for i in range(9):
        if arr[i][y]

board = [list(map(int,input().split())) for _ in range(9)]
check = [False]*9
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            BFS(i, j)