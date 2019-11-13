import sys
sys.setrecursionlimit(10000)

def DFS(i, j):
    global count, visit
    visit[i][j] = 1
    for a in range(4):
        tx = i+dx[a]
        ty = j+dy[a]
        if 0 <= tx < N and 0 <= ty < M and arr[tx][ty] == 1 and not visit[tx][ty]:
            DFS(tx, ty)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]
T = int(input())
for tc in range(T):
    M, N, K = map(int,input().split())
    visit = list([0]*M for _ in range(N))
    arr = list([0]*M for _ in range(N))
    count = 0
    for i in range(K):
        X, Y = map(int,input().split())
        arr[Y][X] = 1
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 1 and not visit[x][y]:
                DFS(x, y)
                count += 1
                # pprint.pprint(arr)
                # pprint.pprint(visit)
    print(count)