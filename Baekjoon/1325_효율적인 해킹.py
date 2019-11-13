from collections import deque
def BFS(x):
    visit = [0 for _ in range(N + 1)]
    Q = deque()
    Q.append(x)
    visit[x] = 1
    cnt = 1
    while Q:
        v = Q.popleft()
        for w in hack[v]:
            if not visit[w]:
                Q.append(w)
                visit[w] = 1
                cnt += 1
    return cnt


N, M = map(int,input().split())
hack = [[] for _ in range(N+1)]
m = 0
result = []
for _ in range(M):
    A, B = map(int,input().split())
    hack[B].append(A)
for j in range(1, N+1):
    c = BFS(j)
    if c == m:
        result.append(j)
        m = c
    elif c > m:
        result = [j]
        m = c
print(*sorted(result))