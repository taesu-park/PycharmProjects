T = int(input())
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
black = 0
white = 0
def othello(n, m, k):
    if k == 1:
        for i in range(8):
            tx, ty = n + dx[i], m + dy[i]
            if 1 <= tx <= N and 1 <= ty <= N and arr[tx][ty] == 2 and arr[tx][ty] != 0:
                while arr[tx][ty] != k:
                    if 1 <= tx <= N and 1 <= ty <= N and arr[tx][ty] == 2 and arr[tx][ty] != 0:
                        arr[tx][ty] = 1
                        tx, ty = tx + dx[i], ty + dy[i]
    if k == 2:
        for i in range(8):
            tx, ty = n + dx[i], m + dy[i]
            if 1 <= tx <= N and 1 <= ty <= N and arr[tx][ty] == 1 and arr[tx][ty] != 0:
                while arr[tx][ty] != k:
                    if 1 <= tx <= N and 1 <= ty <= N and arr[tx][ty] == 1 and arr[tx][ty] != 0:
                        arr[tx][ty] = 2
                        tx, ty = tx + dx[i], ty + dy[i]


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    arr[N//2][N//2] = arr[(N//2)+1][(N//2)+1] = 2
    arr[(N//2)+1][N//2] = arr[N//2][(N//2)+1] = 1
    for _ in range(M):
        x, y, c = map(int,input().split())
        arr[x][y] = c
        othello(x, y, c)
        for o in arr:
            print(o)
        print('---------------')
for v in range(N+1):
    for w in range(N+1):
        if arr[v][w] == 1:
            white += 1
        elif arr[v][w] == 2:
            black += 1
print(white, black)
