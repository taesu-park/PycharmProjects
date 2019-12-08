import sys
sys.setrecursionlimit(100000)

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0

def dfs(x, y, z):
    visit[x][y] = 1
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        tx, ty = x+dx, y+dy
        if tx < 0 or tx >= N or ty < 0 or ty >= N:
            continue
        if not visit[tx][ty] and board[tx][ty] > z:
            dfs(tx, ty, z)


for k in range(max(max(board))):
    visit = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and board[i][j] > k:
                dfs(i, j, k)
                cnt += 1
    ans = max(cnt, ans)
print(ans)