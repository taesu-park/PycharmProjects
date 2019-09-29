board = [list(map(int,input().split())) for _ in range(9)]
xvisit = [False]*10
yvisit = [False]*10
kvisit = [False]*10
def back(x,y,num):
    if num == 9:
        return
    else:
        for a in range(9):
            yvisit[board[x][a]] = True
        for b in range(9):
            xvisit[board[b][y]] = True
        for r in range(3):
            for c in range(3):
                kvisit[board[x+3][y+3]] = True


for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            back(i, j, 0)