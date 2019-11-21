N, L, R = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
dx, dy = [(0, 0, -1, 1), (1, -1, 0, 0)]
Union = []
S = 0


while True:
    for i in range(N):
        for j in range(N):
            for a in range(4):
                tx = i + dx[a]
                ty = j + dy[a]
                if 0 <= tx < N and 0 <= ty < N and L <= abs(board[i][j] - board[tx][ty]) <= R and (tx,ty) not in Union:
                    Union.append((tx,ty))
    for x, y in range(len(Union)):
        S += Union[x][y]