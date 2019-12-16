N, M = map(int,input())
board = [list(map(int,input().split())) for _ in  range(N)]
ans = 0
def back(x,y,n):
    if n == M:
        pass
    else:
        for i in range(N):
            for j in range(N):
                if board[i][j] == 2:
                    back(i,j,n+1)
back(0,0,0)