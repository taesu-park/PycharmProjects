from collections import deque

N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0
c = 0
def solve():
    cheeze = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] >= 2:
                board[i][j] = 0
                cheeze += 1
    return cheeze
def bfs(x, y):
    visit = [[0] * M for _ in range(N)]
    visit[x][y] = 1
    Q = deque()
    Q.append((x,y))
    while Q:
        v, w = Q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tx, ty = v+dx, w+dy
            # if tx < 0 or tx >= N or ty < 0 or ty >= M:
            #     continue
            if 0 <= tx < N and 0 <= ty < M and not visit[tx][ty] and board[tx][ty] == 1:
                board[tx][ty] += 1
            if 0 <= tx < N and 0 <= ty < M and not visit[tx][ty] and board[tx][ty] == 0:
                Q.append((tx,ty))
                visit[tx][ty] = 1


while True:
    bfs(0, 0)
    cheeze = solve()
    if not cheeze:
        break
    else:
        ans += 1
        c = cheeze
print(ans)
print(c)