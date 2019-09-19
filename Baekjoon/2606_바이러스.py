N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]
def DFS(x):
    global count
    visit[x] = True
    for y in sorted(G[x]):
        if not visit[y]:
            DFS(y)
            count += 1


for _ in range(M):
    count = 0
    n, m = map(int,input().split())
    visit = [False]* (N+1)
    G[n].append(m)
    G[m].append(n)
DFS(1)
print(count)