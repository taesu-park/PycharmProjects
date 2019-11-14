def DFS(x, y):
    global island
    tmp.append([x, y])
    visit[x][y] = 1
    for a in range(4):
        tx = x + dx[a]
        ty = y + dy[a]
        if 0 <= tx < N and 0 <= ty < M and not visit[tx][ty] and board[tx][ty]==1:
            DFS(tx, ty)

N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
island = []

for i in range(N):
    for j in range(M):
        tmp = []
        if board[i][j] == 1 and not visit[i][j]:
            DFS(i, j)
            island.append(tmp)

for x in range(len(island)):
    for y in range(len(island[x])):
