import pprint
def DFS(x,y,cnt):
    global MAX, MIN,c
    c = cnt
    visit[x][y] = 1
    for a in range(4):
        tx = x+dx[a]
        ty = y+dy[a]
        if 0 > tx or tx >= N or ty < 0 or ty >= N:
            continue
        if memo[tx][ty] and board[x][y] + 1 == board[tx][ty]:
            c = memo[tx][ty] + 1
            return c
        if not visit[tx][ty] and board[x][y]+1 == board[tx][ty]:
            visit[tx][ty] = 1
            DFS(tx,ty,cnt+1)
    return c
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    memo = [[0]*N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    count = 1
    MAX = 0
    MIN = 0xfffffff
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                c = 0
                memo[i][j] = DFS(i,j,count)
                if c > MAX:
                    MAX = c
                    MIN = board[i][j]
                if c == MAX:
                    MIN = min(board[i][j],MIN)
    print('#{} {} {}'.format(tc,MIN,MAX))
