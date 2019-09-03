from collections import deque


N, M, V = map(int,input().split())
visit = [False for _ in range(N+1)]
G = [[] for _ in range(N+1)]
def DFS(n):
    print(n, end=' ')
    visit[n] = True
    for w in sorted(G[n]):
        if not visit[w]:
            DFS(w)
def BFS(n):
    Visit = [False] * (N+1)
    Q = deque
    Q.append(n)
    Visit[n] = True
    while Q:
        v = Q.popleft()
        for w in sorted(G[v]):
            if not Visit[w]:
                Visit[w] = True
                Q.append(w)
                print(w, end=' ')

for _ in range(M):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

DFS(V)
BFS(V)