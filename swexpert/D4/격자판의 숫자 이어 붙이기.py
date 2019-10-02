def DFS(x,y,k,l):
    global ans
    if k == 7:
        ans.add(l)
        return
    else:
        for i in range(4):
            tx = x+dx[i]
            ty = y+dy[i]
            if 0 <= tx < 4 and 0 <= ty < 4:
                DFS(tx,ty,k+1,l+str(board[tx][ty]))



T = int(input())
for tc in range(1, T+1):
    board = [list(map(int,input().split())) for _ in range(4)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    count = 0
    ans = set()
    for i in range(4):
        for j in range(4):
            DFS(i,j,0,'')
    print('#{} {}'.format(tc,len(ans)))