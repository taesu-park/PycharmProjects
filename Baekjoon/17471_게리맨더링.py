def DFS(x):
    global count
    for i in G[x]:
        if not visit[i]:
            visit[i] = 1
            DFS(i)
    count += 1


N = int(input())
arr = list(map(int,input().split()))
visit = [0]*N
G = [[] for _ in range(N)]
count = 0
for i in range(N):
    tmp = list(map(int,input().split()))
    tmp.pop(0)
    G[i] = tmp
print(G)
for j in range(N):
    DFS(0)
    print(count)