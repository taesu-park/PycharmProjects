from collections import deque

def BFS(x, y):
    Q = deque()
    Q.append(x, y)
    while Q:
        v = Q.popleft()


M, N = map(int,input().split())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
tomato = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            BFS(i, j)