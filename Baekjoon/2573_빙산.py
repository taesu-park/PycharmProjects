from collections import deque

N, M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]
ans = 0
chk = 0

def bfs(x, y):
    global ans, chk
    Q = deque()
    Q.append((x, y))
    ice = [[0] * M for _ in range(N)]
    visit[x][y] = 1
    while Q:
        v, w = Q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tx , ty = v+dx, w+dy
            if tx < 0 or tx >= N or ty < 0 or ty >= M:
                continue
            if board[tx][ty] == 0:
                ice[v][w] += 1
            if board[tx][ty] >= 1 and not visit[tx][ty]:
                visit[tx][ty] = 1
                Q.append((tx,ty))
    for i in range(N):
        for j in range(M):
            if ice[i][j]:
                board[i][j] -= ice[i][j]
                if board[i][j] <= 0:
                    board[i][j] = 0
    chk = 1
    return chk

while True:
    c = 0
    visit = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not board[i][j]:
                continue
            if board[i][j] and not visit[i][j]:
                bfs(i,j)

    ans += 1