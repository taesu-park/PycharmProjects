from collections import deque

N, M = map(int,input())

board = [list(map(int,input().split())) for _ in range(M)]
visit = [[0]*N for _ in range(M)]


def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    while Q:
        v, w = Q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]
            tx , ty = v+dx, w+dy
            if tx < 0 or tx >= N or ty < 0 or ty >= M:
                continue
            if board[tx][ty] == 0:
                Q.append((tx,ty))

for i in range(N):
    for j in range(M):
        if board[i][j] and not visit[i][j]:
            bfs(i, j)