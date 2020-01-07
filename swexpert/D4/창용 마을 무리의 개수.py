def dfs(x):
    visit[x] = 1
    for i in range(len(G[x])):
        if not visit[G[x][i]]:
            dfs(G[x][i])
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    G = [list() for _ in range(N+1)]
    visit = [0 for _ in range(N+1)]
    cnt = 0
    for _ in range(M):
        v, w = map(int,input().split())
        G[v].append(w)
        G[w].append(v)
    for i in range(1, N+1):
        if not visit[i] and G[i]:
            cnt += 1
            dfs(i)
        if not visit[i]:
            cnt +=1
    print('#{} {}'.format(tc,cnt))