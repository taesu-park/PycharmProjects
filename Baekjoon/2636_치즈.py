from collections import deque

N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
# air = [[0]*M for _ in range(N)]

def bfs(x, y):
    visit[x][y] = 1
    q = deque()
    q.append((x,y))
    if q:
        v, w = q.popleft()


for i in range(N):
    for j in range(M):
        if (board[i][j] == 0) and (i == 0 or j == 0 or j == M or i == N):
            if not visit[i][j]:
                bfs(i, j)

