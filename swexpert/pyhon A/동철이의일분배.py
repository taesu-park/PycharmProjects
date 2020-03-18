def back(x,l):
    global MAX
    if l < MAX:
        return
    if x == N:
        if l > MAX:
            MAX = l
        return
    else:
        for j in range(N):
            if not visit[j]:
                visit[j] = 1
                back(x+1,l*board[x][j]*0.01)
                visit[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    visit = [0]*N
    MAX = 0.01
    back(0,1)
    print('#{} {:.6f}'.format(tc,(MAX*100)))