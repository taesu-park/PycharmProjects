def dfs(x, y, z, v, c):
    global MAX
    if c >= MAX:
        MAX = c
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        tx, ty = x + dx, y + dy
        if tx < 0 or tx >= R or ty < 0 or ty >= C:
            continue
        if board[tx][ty] not in z and not v[tx][ty]:
            v[tx][ty] = 1
            z.append(board[tx][ty])
            dfs(tx, ty, z, v, c + 1)
            z.remove(board[tx][ty])
            v[tx][ty] = 0

R, C = map(int, input().split())
board = list(list(input()) for _ in range(R))
visit = [[0] * C for _ in range(R)]
visit[0][0] = 1
cnt = 0
MAX = 0

dfs(0, 0, [board[0][0]], visit, cnt)
print(MAX+1)
