from collections import deque


a = 0
M, N, H = map(int,input().split())
tomato = []
cnt = -1
visit = [[[0]*M for _ in range(N)] for _ in range(H)]
dx = (0, 0, -1, 1, 0, 0)
dy = (1, -1, 0, 0, 0, 0)
dz = (0, 0, 0, 0, 1, -1)
for x in range(H):
    tomato.append([list(map(int,input().split())) for _ in range(N)])
Q = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 1 and not visit[k][i][j]:
                Q.append((k, i, j))
                visit[k][i][j] = 1
while Q:
    q = len(Q)
    cnt += 1
    for _ in range(q):
        k, i, j = Q.popleft()
        for a in range(6):
            tz = k + dz[a]
            tx = i + dx[a]
            ty = j + dy[a]
            if 0 <= tz < H and 0 <= tx < N and 0 <= ty < M and tomato[tz][tx][ty]==0 and not visit[tz][tx][ty]:
                tomato[tz][tx][ty] = 1
                visit[tz][tx][ty] = 1
                Q.append((tz, tx, ty))

for k_1 in range(H):
    for i_1 in range(N):
        for j_1 in range(M):
            if tomato[k_1][i_1][j_1] == 0:
                cnt = -1
                a = 1
                print(cnt)
                break
        if a == 1:
            break
    if a == 1:
        break
if a != 1:
    print(cnt)