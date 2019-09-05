N = int(input())

arr = [[0]*N for _ in range(N)]
ans = 0
visit = ([False]*N for _ in range(N))
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
def Queen(x, y, k):
    if
    for i in range(N):
        for j in range(N):
            for p in range(8):
                tx, ty = i+dx[p], j+dy[p]
                while tx >= 0 and tx < N and ty >= 0 and ty < N:
                    visit[tx][ty] = True
