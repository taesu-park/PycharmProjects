import sys
sys.setrecursionlimit(10000)
N = int(input())
arr = [list(input()) for _ in range(N)]
visit = [[False]*N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = ccount = 0
def DFS(n, m, k):
    visit[n][m] = True
    for x in range(4):
        tx = n + dx[x]
        ty = m + dy[x]
        if tx >= 0 and tx < N and ty >= 0 and ty < N and not visit[tx][ty] and arr[tx][ty] == k:
            DFS(tx, ty, arr[tx][ty])

for i in range(N):
    for j in range(N):
        if (arr[i][j] == 'R' or arr[i][j] == 'B' or arr[i][j] == 'G')and not visit[i][j]:
            DFS(i, j, arr[i][j])
            count += 1
for r in range(N):
    for c in range(N):
        # if arr[r][c] == 'G':
        #     arr[r][c] = 'R'
        arr[r][c] = arr[r][c].replace('G','R')
visit = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if (arr[i][j] == 'R' or arr[i][j] == 'B')and not visit[i][j]:
            DFS(i, j, arr[i][j])
            ccount += 1
print(count, ccount)