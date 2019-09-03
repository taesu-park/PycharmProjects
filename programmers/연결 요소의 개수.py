import sys
sys.setrecursionlimit(10000)
N, M = map(int,sys.stdin.readline().split())
G = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
count = 0
def DFS(v):
    visit[v] = True
    for w in G[v]:
        if not visit[w]:
            DFS(w)

for _ in range(M):
    u, v = map(int,sys.stdin.readline().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, len(G)):
    if visit[i] == False:
        DFS(i)
        count += 1
print(count)