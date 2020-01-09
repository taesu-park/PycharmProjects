def bfs():
    cnt = 10
    while cnt:
        Q = len(q)
        stop, flag = 0, 0
        cnt -= 1
        if flag:
            pass
        for _ in range(Q):
            x, y, b = q.popleft()
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                while not stop:
                    tx, ty = x+dx, y+dy
                    if board[tx][ty] == '#':
                        stop = 1
                        q.append((tx-dx,ty-dy,b))
                    elif board[tx][ty] == 'O':
                        flag = 1
from collections import deque
N, M = map(int,input().split())
board = list(list(input()) for _ in range(N))
q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            q.append((i,j,1))
        elif board[i][j] == 'B':
            q.append((i,j,2))
bfs()