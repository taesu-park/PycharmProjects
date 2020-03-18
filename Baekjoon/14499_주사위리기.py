def rotate(dice, tx,ty,k):
    t = [0]*4
    if k == 1 or k == 4:
        for i in range(4):
            t[i%4] = dice[(i+1)%4]
    else:
        for i in range(4):
            t[(i+1)%4] = dice[i%4]
    if board[tx][ty]:
        t[0] = board[tx][ty]
        board[tx][ty] = 0
    else:
        board[tx][ty] = t[0]
    dice = t
    print(dice[2])
    return dice
def solve(x_1,y_1,k):
    global x, y, dice1, dice2
    tx, ty = dx[k-1]+x_1, dy[k-1]+y_1
    if tx < 0 or tx >= N or ty < 0 or ty >= M:
        return
    else:
        if k == 1 or k == 2:
            dice1 = rotate(dice1, tx,ty,k)
            dice2[0], dice2[2] = dice1[0], dice1[2]
        else:
            dice2 = rotate(dice2, tx,ty,k)
            dice1[0], dice1[2] = dice2[0], dice2[2]
        x, y = tx, ty
N, M , x, y , K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dx, dy = (0,0,-1,1), (1,-1,0,0)
dice1 = [0, 0, 0, 0]
dice2 = [0, 0, 0, 0]
dice1[0] = board[x][y]
dice2[0] = board[x][y]
k = list(map(int,input().split()))
for i in range(K):
    a = k[i]
    solve(x,y,a)