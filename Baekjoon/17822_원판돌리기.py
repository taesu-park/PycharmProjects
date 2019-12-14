from copy import deepcopy
def rotate(x, a, b):
    d_board = deepcopy(board)
    if a == 0:
        for i in range(M):
            board[x][i] = d_board[x][(i+M-b)%M]
    else:
        for j in range(M):
            board[x][j] = d_board[x][(j+M+b)%M]
# def check():


N, M, T = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
print(board)
for _ in range(T):
    x, d, k = map(int,input().split())
    for i in range(N):
        if not (i+1) % x:
            rotate(i, d, k)
            print(board)
            # check()




# def solve():
#     pass


