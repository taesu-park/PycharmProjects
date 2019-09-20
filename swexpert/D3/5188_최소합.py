T = int(input())
dx = [1, 0]
dy = [0, 1]
result = []
coordinate = []
def DFS(n,m):
    global N
    for x in range(2):
        tx = n + dx[x]
        ty = m + dy[x]
        if tx >= 0 and tx < N and ty >= 0 and ty < N:
            result.append(arr[tx][ty])


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
