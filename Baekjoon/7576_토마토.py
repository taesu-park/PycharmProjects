from collections import deque

# def BFS(x):
#     global cnt
#     Q = deque()
#     Q.append([x[0], x[1]])
#     while Q:
#         v = Q.popleft()
#         for i in range(4):
#             tx = v[0] + dx[i]
#             ty = v[1] + dy[i]
#             if 0 <= tx < N and 0 <= ty < M and tomato[tx][ty] == 0:
#                 tomato[tx][ty] = 1
#                 Q.append([tx,ty])
#         cnt += 1



M, N = map(int,input().split())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
tomato = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
cnt = 0
Q = deque()
a = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            visit[i][j] = 1
            Q.append([i,j])
while Q:
    cnt += 1
    q = len(Q)
    for _ in range(q):
        v = Q.popleft()
        for i in range(4):
            tx = v[0] + dx[i]
            ty = v[1] + dy[i]
            if 0 <= tx < N and 0 <= ty < M and tomato[tx][ty] == 0 and not visit[tx][ty]:
                tomato[tx][ty] = 1
                Q.append([tx, ty])
for x in range(N):
    for y in range(M):
        if tomato[x][y] == 0:
            a = 1
            print(-1)
            break
    if a == 1:
        break


if a != 1:
    print(cnt-1)



