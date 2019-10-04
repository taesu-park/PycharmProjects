def DFS(x,y,cnt):
    global MAX, MIN
    if cnt >= MAX:
        MAX = cnt
        if board[x][y] < MIN:
            MIN = board[x][y]
    visit[x][y] = 1
    for a in range(4):
        tx = x+dx[a]
        ty = y+dy[a]
        if 0 <= tx < N and 0 <= ty < N and not visit[tx][ty] and board[x][y]+1 == board[tx][ty]:
            visit[tx][ty] = 1
            DFS(tx,ty,cnt+1)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    count = 1
    MAX = 0
    MIN = 0xfffffff
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            visit = [[0]*N for _ in range(N)]
            DFS(i,j,count)
    print('#{} {} {}'.format(tc,MIN,MAX))
