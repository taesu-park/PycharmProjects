def DFS(x):
    global visit, count
    visit[x] = 1
    for w in G[x]:
        if not visit[w]:
            DFS(w)
    count += 1
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    visit = [0]*(N+1)
    G = [[] for _ in range(N+1)]
    count = 0
    for _ in range(M):
        v, w = map(int,input().split())
        G[v].append(w)
        G[w].append(v)
    for i in range(1, M+1):
        DFS(i)
