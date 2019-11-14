import sys
sys.setrecursionlimit(10000)

def check(x, y):
    global visit, cnt
    visit[x][y] = 1
    cnt += 1
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        tx , ty =  x+ dx, y+ dy
        if 0 <= tx < M and 0 <= ty < N and not visit[tx][ty] and board[tx][ty] == 0:
            check(tx, ty)


M, N, K = map(int,input().split())
board = [[0]*N for _ in range(M)]
visit = [[0]*N for _ in range(M)]
result = []
cnt = 0
for _ in range(K):
    x_1, y_1, x_2, y_2 = map(int,input().split())
    for i in range(y_1, y_2):
        for j in range(x_1, x_2):
            board[i][j] = 1

for x in range(M):
    for y in range(N):
        if board[x][y] == 0 and not visit[x][y]:
            check(x,y)
            result.append(cnt)
            cnt = 0
print(len(result))
print(*sorted(result))