N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]
def DFS(x):
    visit[x] = True
    if not G[x]:
        DFS(x)


for _ in range(M):
    n, m = map(int,input().split())
    visit = [[False] for _ in range(N+1)]
    G[n].append(m)
DFS(1)