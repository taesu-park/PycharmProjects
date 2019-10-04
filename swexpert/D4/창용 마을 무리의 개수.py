T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    visit = [0]*(N+1)
    G = [0]*(N+1)
    for _ in range(M):
        v, w = map(int,input().split())
        G[v].append(w)
    print(G)