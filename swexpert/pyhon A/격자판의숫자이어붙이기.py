def DFS(n,m,k):
    global result
    if len(k) == 7:
        result.add(k)
        return
    else:
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            tx, ty = n+dx, m+dy
            if tx < 0 or tx >= 4 or ty < 0 or ty >= 4:
                continue
            else:
                DFS(tx,ty,k+str(board[tx][ty]))
def solve():
    for i in range(4):
        for j in range(4):
            DFS(i,j,str(board[i][j]))

T = int(input())
for tc in range(1, T+1):
    board = [list(map(int,input().split())) for _ in range(4)]
    result = set()
    solve()
    print('#{} {}'.format(tc,len(result)))