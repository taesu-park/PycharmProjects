def bfs():
    q.append((sx,sy,0))
    dist[sx][sy] = 1
    while q:
        x,y,f = q.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            tx, ty = x+dx, y+dy
            if tx < 0 or tx >= h or ty < 0 or ty >= w:
                if f == 1:
                    continue
                return dist[x][y]
            if dist[tx][ty] or board[tx][ty] == '#':
                continue
            dist[tx][ty] = dist[x][y] + 1
            q.append((tx,ty,f))
    return 'IMPOSSIBLE'
from collections import deque
T = int(input())
for tc in range(1, T+1):
    w,h = map(int,input().split())
    board = list(list(input()) for _ in range(h))
    dist = [[0]*w for _ in range(h)]
    q = deque()
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                sx, sy = i, j
            elif board[i][j] == '*':
                dist[i][j] = 1
                q.append((i,j,1))
    print(bfs())