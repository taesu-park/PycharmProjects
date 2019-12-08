import sys
sys.setrecursionlimit(10000)

N, L, R = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
moving = [[0]*N for _ in range(N)]
dx, dy = [(0, 0, -1, 1), (1, -1, 0, 0)]
cnt = 0

def dfs(x, y):
    global cnt
    visit[x][y] = 1
    population = board[x][y]
    for a in range(4):
        tx = x + dx[a]
        ty = y + dy[a]
        if tx < 0 or tx >= N or ty < 0 or ty >= N:
            continue
        if not visit[tx][ty] and L <= abs(board[tx][ty]-board[x][y]) <= R:
            moving[tx][ty] = 1
            cnt += 1
            population += dfs(tx, ty)
    return population

def migrate(p):
    for i in range(N):
        for j in range(N):
            if moving[i][j]:
                board[i][j] = p
                moving[i][j] = 0

def solve():
    global cnt, visit
    ans = 0
    while True:
        moved = False
        visit = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not visit[i][j]:
                    cnt = 1
                    population = dfs(i,j) // cnt
                    if cnt > 1:
                        board[i][j] = population
                        migrate(population)
                        moved = True
        if moved:
            ans += 1
        else:
            break
    print(ans)
solve()


