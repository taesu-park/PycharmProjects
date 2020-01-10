def bfs():
    cnt = 10
    while cnt:
        Q = len(q)
        stop, flag = 0, 0
        cnt -= 1
        if flag:
            pass
        for _ in range(Q):
            x1, y1, b = q.popleft()
            x2, y2, b = q.popleft()
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                tx1, ty1 = x1 + dx, y1 + dy
                tx2, ty2 = x2 + dx, y2 + dy
                if board[tx1][ty1] == board[tx2][ty2] == '#':
                    continue
                else:
                    while not stop:
                        tx1, ty1 = x1+dx, y1+dy
                        tx2, ty2 = x2+dx, y2+dy

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

