
dx = [0, 0, -1]
dy = [-1, 1, 0]
def DFS(i, j):
    # print(i,j)
    global x
    if i == 0:
        x = j
        print(x)


    visit[i][j] = True

    for a in range(3):
        tx = i + dx[a]
        ty = j + dy[a]
        if tx >= 0 and tx < 100 and ty >= 0 and ty < 100 and arr[tx][ty] == 1 and not visit[tx][ty]:
            DFS(tx, ty)
        if x:
            return


for _ in range(10):
    tc = int(input())
    x = False
    arr = [list(map(int,input().split())) for _ in range(100)]
    visit = [[False]*100 for _ in range(100)]
    for r in range(100):
        for c in range(100):
            if arr[r][c] == 2:
                DFS(r, c)

