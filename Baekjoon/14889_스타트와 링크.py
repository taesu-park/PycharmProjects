N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [0 for _ in range(N)]
A, B = 0, 0
ans = 0xfffffff
def back(x, y, z):
    global ans, A, B
    if z == N:
        if abs(A - B) < ans:
            ans = abs(A - B)
        return
    if z == (N // 2):
        B += board[x][y]
    else:
        A += board[x][y]
    for i in range(z, N):
        for j in range(N):
            if i == j or visit[j]:
                continue
            else:
                visit[j] = 1
                back(i, j, z + 1)
                visit[j] = 0
back(0, 0, 0)
print(ans)