def back(n, m, k, p):
    global SUM

    if k == 0:
        SUM += p
    else:
        for x in range(4):
            tx = n + dx[x]
            ty = m + dy[x]
            if not visit[tx][ty]:
                visit[tx][ty] = True
                back(tx, ty, k-1, p*(arr[x+1]/100))
                visit[tx][ty] = False

arr = list(map(int,input().split()))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
SUM = 0
M = arr[0]*2+1
visit = [[False]*M for _ in range(M)]
N = len(visit)//2
visit[N][N] = True
back(N,N,N, 1)
print(SUM)