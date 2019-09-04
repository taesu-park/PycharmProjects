from collections import deque
import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int,sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
count = 1
def BFS(n, m):
    global count

    Q = deque()
    Q.append((n,m))
    visit[n][m] = 1

    while Q:
        for _ in range(len(Q)):
            u, v = Q.popleft()
            if (u, v) == (N-1, M-1):
                return
            for x in range(4):
                tx , ty = u+dx[x], v + dy[x]
                if tx >= 0 and tx < N and ty >= 0 and ty < M:
                    if not visit[tx][ty] and int(arr[tx][ty]) == 1:
                        visit[tx][ty] = True
                        Q.append((tx,ty))
        count += 1



        

BFS(0,0)

print(count)