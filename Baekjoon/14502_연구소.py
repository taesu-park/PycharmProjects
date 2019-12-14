from copy import deepcopy
from collections import deque
N, M = map(int,input().split())
d_board = [list(map(int,input().split())) for _ in range(N)]
ans = 0

def bfs(x, y, check, board):
    Q = deque()
    Q.append((x,y))
    while Q:
        v, w = Q.popleft()
        for dx, dy in [(0,-1),(0,1),(1,0),(-1,0)]:
            tx, ty = v+dx, w+dy
            if tx < 0 or tx >= N or ty < 0 or ty >= M:
                continue
            if board[tx][ty] == 0 and not check[tx][ty]:
                check[tx][ty] = 1
                board[tx][ty] = 2
                Q.append((tx,ty))

def back(idx):
    global ans
    board = deepcopy(d_board)
    check = [[0]*M for _ in range(N)]
    if idx == 3:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 2 and not check[i][j]:
                    check[i][j] = 1
                    bfs(i, j, check, board)
        for i_1 in range(N):
            for j_1 in range(M):
                if board[i_1][j_1] == 0:
                    cnt += 1
        ans = max(cnt, ans)
        return
    for x in range(N):
        for y in range(M):
            if d_board[x][y] == 0:
                d_board[x][y] = 1
                back(idx+1)
                d_board[x][y] = 0
back(0)
print(ans)