def DFS(v):
    visit[v] = 1

    for w in G[v]:
        if not visit[w]:
            DFS(w)


T = int(input())

for tc in range(1, T+1):
    V, E = map(int,input().split())
    G = [[] for _ in range(V+1)]
    visit = [0 for _ in range(V+1)]

    for _ in range(1, E+1):
        u, v = map(int,input().split())
        G[u].append(v)
    x, y = map(int,input().split())

    DFS(x)
    print('#{} {}'.format(tc,visit[y]))