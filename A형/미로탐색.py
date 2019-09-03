from collections import deque


N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
print(visit)

def BFS(n, m, v):
    visit = [[0] * M for _ in range(N)]
    Q = deque()
    Q.append((n,m))
    visit[n][m] = 1
    while Q:
        
for i in range(N):
    for j in range(M):
        if int(arr[i][j]) == 1 and not visit[i][j]:
            BFS(i,j)

