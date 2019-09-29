from collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n, m = map(int,input().split())
    i, j = map(int,input().split())
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    Q = deque()
    count = 0
    a = 0
    visit = [[False]*N for _ in range(N)]
    Q.append((n, m))

    while Q:
        if a:
            break
        for _ in range(len(Q)):
            v, w = Q.popleft()
            visit[v][w] = True
            if (v, w) == (i, j):
                a = 1
                print(count)
                break
            else:
                for x in range(8):
                    tx = v + dx[x]
                    ty = w + dy[x]
                    if 0 <= tx < N and 0 <= ty < N and not visit[tx][ty]:
                        Q.append((tx,ty))
        count += 1
