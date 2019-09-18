dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(n, m):
    global a

    visit[n][m] = True
    for x in range(4):
        tx = n+dx[x]
        ty = m+dy[x]
        if tx >= 0 and tx < N and ty >= 0 and ty < N and arr[tx][ty] == 0 and not visit[tx][ty]:
            DFS(tx,ty)
        if tx >= 0 and tx < N and ty >= 0 and ty < N and arr[tx][ty] == 3:
            a = 1
            return




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visit = [[False]*N for _ in range(N)]
    arr = [list(map(int,input())) for _ in range(N)]
    a = 1000
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                DFS(i, j)
        if not a:
            break
    if a==1:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))