def check_left(n,d):
    if n < 0:
        return
    if board[n][2] != board[n+1][6]:
        check_left(n-1, -d)
        rotate(n, -d)

def check_right(n,d):
    if n > 3:
        return
    if board[n][6] != board[n-1][2]:
        check_right(n+1, -d)
        rotate(n, -d)
def rotate(n,d):
    t = [0]*8
    if d == 1:
        for i in range(8):
            t[(i+1)%8] = board[n][i]
    else:
        for i in range(8):
            t[(i)%8] = board[n][(i+1)%8]
    for i in range(8):
        board[n][i] = t[i]
board = [list(input()) for _ in range(4)]
K = int(input())
ans = 0
for _ in range(K):
    num, dir = map(int,input().split())
    check_left(num-2, dir)
    check_right(num, dir)
    rotate(num-1, dir)
for i in range(4):
    if board[i][0] == '1':
        ans += (1<<i)
print(ans)